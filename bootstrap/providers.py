"""
Service Providers Configuration
Define which service providers should be loaded

To add a new provider, simply append it to the CORE_PROVIDERS list:
    CORE_PROVIDERS.append('your.module.path.YourServiceProvider')

Note: Middleware is now configured in config/middleware.py (GLOBAL_MIDDLEWARE, ROUTE_MIDDLEWARE)
"""

# Core framework providers (loaded in order)
CORE_PROVIDERS = [
    'larasanic.providers.logging_service_provider.LoggingServiceProvider',
    'larasanic.providers.cache_service_provider.CacheServiceProvider',
    'larasanic.providers.database_service_provider.DatabaseServiceProvider',
    'larasanic.providers.http_service_provider.HttpServiceProvider',
    'larasanic.providers.routing_service_provider.RoutingServiceProvider',
    'larasanic.providers.auth_service_provider.AuthServiceProvider',
    'larasanic.providers.session_service_provider.SessionServiceProvider',
    'larasanic.providers.websocket_service_provider.WebSocketServiceProvider',
    'larasanic.providers.blade_service_provider.BladeServiceProvider',
]
