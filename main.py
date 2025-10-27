#!/usr/bin/env python3
"""
Application Entry Point
Run the Sanic application with the framework
"""
# Import support classes (auto-loads .env)
from larasanic.support import Storage, EnvHelper, Config

from bootstrap.app import create_app

# Create application
app = create_app()

# Export Sanic app for CLI (`python -m sanic main:sanic_app`)
sanic_app = app.sanic_app

if __name__ == '__main__':
    # Run the Sanic server
    app.run(
        host=Config.get('app.APP_HOST', '0.0.0.0'),
        port=Config.get('app.APP_PORT', 8000),
        debug=Config.get('app.APP_DEBUG', False),
        auto_reload=Config.get('app.APP_DEBUG', False)
    )
