"""
Application Configuration
Main application settings
"""
from larasanic.support import Storage, EnvHelper

# Application name
APP_NAME = EnvHelper.get('APP_NAME', 'Framework App')

# Environment
APP_ENV = EnvHelper.get('APP_ENV', 'local')  # local, staging, production
APP_DEBUG = EnvHelper.get('APP_DEBUG', 'true').lower() == 'true'

# Server configuration
APP_HOST = EnvHelper.get('APP_HOST', '0.0.0.0')
APP_PORT = int(EnvHelper.get('APP_PORT', 8000))

# URL configuration
APP_URL = EnvHelper.get('APP_URL', f'http://localhost:{APP_PORT}')

# Package discovery
APP_PACKAGE_DISCOVERY = EnvHelper.get('APP_PACKAGE_DISCOVERY', 'false').lower() == 'true'

# Routing configuration
USE_BLUEPRINT_ROUTING = EnvHelper.get('USE_BLUEPRINT_ROUTING', 'true').lower() == 'true'

# Timezone
TIMEZONE = EnvHelper.get('TIMEZONE', 'UTC')

# Rate Limiting
RATE_LIMIT_DEFAULT = int(EnvHelper.get('RATE_LIMIT_DEFAULT', 100))
RATE_LIMIT_WINDOW = int(EnvHelper.get('RATE_LIMIT_WINDOW', 60))

# Compression
COMPRESSION_ENABLED = EnvHelper.get('COMPRESSION_ENABLED', 'true').lower() == 'true'
COMPRESSION_MIN_SIZE = int(EnvHelper.get('COMPRESSION_MIN_SIZE', 1024))
COMPRESSION_LEVEL = int(EnvHelper.get('COMPRESSION_LEVEL', 6))
MINIFY_HTML = EnvHelper.get('MINIFY_HTML', 'true').lower() == 'true'

# Security Logging
SECURITY_LOGGING_ENABLED = EnvHelper.get('SECURITY_LOGGING_ENABLED', 'true').lower() == 'true'

# Logging Configuration - Allowed Logger Handlers
ALLOWED_LOGGING_HANDLERS = {
    'application': {
        'name': None,  # None = root logger (catches all module loggers)
        'file_name': 'application',  # File name for root logger
        'filter_sensitive': True,
        'level': 'INFO',
    },
    'security': {
        'name': 'security',
        'filter_sensitive': True,
        'level': 'WARNING',
    },
    'malformed': {
        'name': 'malformed',
        'filter_sensitive': True,
        'level': 'WARNING',
    },
}

# WebSocket Configuration
WS_ENABLED = EnvHelper.get_bool('WS_ENABLED', True)
WS_PATH = EnvHelper.get('WS_PATH', '/ws/live')
WS_PING_INTERVAL = int(EnvHelper.get('WS_PING_INTERVAL', 20))
WS_PING_TIMEOUT = int(EnvHelper.get('WS_PING_TIMEOUT', 10))
WS_CLOSE_TIMEOUT = int(EnvHelper.get('WS_CLOSE_TIMEOUT', 10))