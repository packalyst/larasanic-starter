"""
Middleware Configuration (Laravel Kernel Style)
Define global and route middleware

Matches Laravel's app/Http/Kernel.php structure:
https://laravel.com/docs/12.x/middleware

Middleware Layers:
1. GLOBAL_MIDDLEWARE - Runs on EVERY request before routing
2. ROUTE_MIDDLEWARE - Only runs on routes that specify it via .middleware()
"""

# =============================================================================
# Global Middleware (available for blueprints)
# =============================================================================
# These middlewares are available globally and can be assigned to blueprints
# via MIDDLEWARE_GROUPS below. They run via Sanic's global middleware system.
#
# Format: {name: class_path}
# The 'name' is used in MIDDLEWARE_GROUPS to assign middleware to blueprints

GLOBAL_MIDDLEWARE = {
    'security_headers': 'larasanic.middleware.security_headers_middleware.SecurityHeadersMiddleware',
    'cors': 'larasanic.middleware.cors_middleware.CorsMiddleware',
    'rate_limit': 'larasanic.middleware.rate_limit_middleware.RateLimitMiddleware',
    'csrf': 'larasanic.middleware.csrf_middleware.CsrfMiddleware',
    'compression': 'larasanic.middleware.compression_middleware.CompressionMiddleware',
    'security_logger': 'larasanic.middleware.security_logger_middleware.SecurityLoggerMiddleware',
}

# =============================================================================
# Route Middleware (Laravel-style)
# =============================================================================
# Only runs when explicitly specified on routes:
#   Route.get('/dashboard', handler).middleware('auth')
#   Route.get('/login', handler).middleware('guest')
#
# Each route builds its own middleware pipeline based on .middleware() calls
# This is exactly how Laravel works!

ROUTE_MIDDLEWARE = {
    # Authentication middleware - require logged in user
    # Usage: Route.get('/dashboard', handler).middleware('auth')
    'auth': 'larasanic.middleware.auth_middleware.AuthMiddleware',

    # Guest middleware - only allow non-authenticated users
    # Usage: Route.get('/login', handler).middleware('guest')
    'guest': 'larasanic.middleware.guest_middleware.GuestMiddleware',

    # SPA middleware - example middleware for testing nested groups
    # Usage: Route.middleware('spa').group(...)
    'spa': 'larasanic.middleware.spa_middleware.SpaMiddleware',

    # Add more route middleware here:
}

# =============================================================================
# Middleware Groups (Laravel-style)
# =============================================================================
# Controls which GLOBAL middleware runs on which blueprint
# (follows Laravel's app/Http/Kernel.php middleware groups pattern)
#
# This determines which middleware from GLOBAL_MIDDLEWARE applies to each blueprint.
# ServiceMiddleware checks this to filter global middleware by blueprint.
#
# Usage:
#   - routes/web.py -> runs 'web' group middleware
#   - routes/api.py -> runs 'api' group middleware
#   - routes/ws.py -> runs 'ws' group middleware
#
# Note: Route-specific middleware (like 'auth', 'guest') are set on individual
# routes via .middleware() calls, NOT here.

MIDDLEWARE_GROUPS = {
    'web': [
        # Global middleware that runs on ALL web routes
        'security_headers',
        'csrf',
        'rate_limit',
        'compression',
        'security_logger',
    ],
    'api': [
        # Global middleware that runs on ALL API routes
        'security_headers',
        'cors',
        'rate_limit',
        'compression',
        'security_logger',
    ],
    'ws': [
        # Global middleware that runs on ALL WebSocket routes
        'security_headers',
    ],
}