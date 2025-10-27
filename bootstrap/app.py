import sys

# Import support classes first
from larasanic.support import Storage

# Add project root to path
project_root = Storage.base()
sys.path.insert(0, str(project_root))

from larasanic.application import Application
from larasanic.package_manager import PackageManager
from larasanic.validation import ValidateApp

def create_app() -> Application:
    # Create application
    app = Application(base_path=str(project_root))

    # Load configuration
    from larasanic.support.facades import Facade
    from bootstrap import providers
    from config import packages as pkg_config
    from larasanic.support.config import Config
    
    # Initialize facades with application instance
    Facade.set_app(app)
    
    # Register core service providers
    from larasanic.support import ClassLoader

    for provider_class_path in providers.CORE_PROVIDERS:
        provider_class = ClassLoader.load(provider_class_path)
        app.register_provider(provider_class)
    
    # Discover and load packages
    if Config.get('app.APP_PACKAGE_DISCOVERY', False):
        package_manager = PackageManager(app)
        package_manager.discover()
        # Load enabled packages
        for package_name in pkg_config.ENABLED_PACKAGES:
            try:
                package_manager.load_package(package_name)
            except Exception as e:
                print(f"Warning: Could not load package '{package_name}': {e}")

    # Boot the application (providers can register routes in boot())
    app.boot()

    # Load routes (includes both file routes and provider routes)
    register_static_routes(app)
    register_routes(app)
    
    # Register all middlewares with Sanic (after all providers have booted)
    app.make('middleware_manager').register_with_sanic()

    return app

def register_static_routes(app):
    # Static files
    app.sanic_app.static("/static", "./public", name="static_public")

def register_routes(app):
    """
    Register application routes using blueprint-based system
    """
    from larasanic.routing.blueprint_loader import BlueprintLoader
    BlueprintLoader().register_sanic_routes()