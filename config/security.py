"""
Security Constants
Application-wide security configuration constants
"""
from larasanic.support import EnvHelper

# Token TTLs (in seconds)
ACCESS_TOKEN_TTL_SECONDS = int(EnvHelper.get('ACCESS_TOKEN_TTL_SECONDS', 900))
REFRESH_TOKEN_TTL_SECONDS = int(EnvHelper.get('REFRESH_TOKEN_TTL_SECONDS', 2592000))

# JWT Configuration
JWT_ALGORITHM = "RS256"

# Token Types
TOKEN_TYPE_ACCESS = "access"
TOKEN_TYPE_REFRESH = "refresh"

# Cookie Names
COOKIE_ACCESS_TOKEN_NAME = "access_token"
COOKIE_REFRESH_TOKEN_NAME = "refresh_token"
CSRF_COOKIE_NAME = "csrf_token"

# Header Names
CSRF_HEADER_NAME = "X-CSRF-Token"
SPA_REQUEST_HEADER_NAME = "X-SPA-Request"  # Used for optimized SPA request detection

# CORS Configuration
CORS_ENABLED = EnvHelper.get('CORS_ENABLED', 'true').lower() == 'true'
ALLOWED_ORIGINS = EnvHelper.get('ALLOWED_ORIGINS', '').split(',')

# CSRF Configuration
# IMPORTANT: Enable CSRF protection for web applications with state-changing operations
# Set CSRF_ENABLED=true in .env to enable CSRF protection
CSRF_ENABLED = EnvHelper.get('CSRF_ENABLED', 'false').lower() == 'true'
CSRF_SECRET = EnvHelper.get('CSRF_SECRET', '')
if not CSRF_SECRET and CSRF_ENABLED:
    import warnings
    warnings.warn(
        "CSRF_SECRET not found in environment. "
        "Please set it in .env for production use. "
        "CSRF protection is enabled but will not work without a secret."
    )

# Password Hashing
# Bcrypt rounds (4-31): 4 = ~1ms, 6 = ~5ms, 8 = ~20ms, 10 = ~80ms, 12 = ~330ms
# Development: 6-8 (fast), Production: 12 (secure)
BCRYPT_ROUNDS = int(EnvHelper.get('BCRYPT_ROUNDS', 6))

# WebSocket Auth
WS_AUTH_CLOSE_CODE = 4001
WS_PROTOCOL_PREFIX = "bearer"

# Security Headers Configuration
# These headers provide defense-in-depth against common web vulnerabilities
X_FRAME_OPTIONS = EnvHelper.get('X_FRAME_OPTIONS', 'DENY')  # DENY, SAMEORIGIN, or ALLOW-FROM
X_CONTENT_TYPE_OPTIONS = EnvHelper.get('X_CONTENT_TYPE_OPTIONS', 'nosniff')
X_XSS_PROTECTION = EnvHelper.get('X_XSS_PROTECTION', '1; mode=block')

# Content Security Policy (CSP)
CSP_ENABLED = EnvHelper.get('CSP_ENABLED', 'true').lower() == 'true'
CSP_POLICY = EnvHelper.get('CSP_POLICY', None)  # Custom CSP policy (None = use secure defaults)

# HTTP Strict Transport Security (HSTS)
# IMPORTANT: Only enable HSTS if your application is served over HTTPS
HSTS_ENABLED = EnvHelper.get('HSTS_ENABLED', 'false').lower() == 'true'  # Disabled by default (requires HTTPS)
HSTS_MAX_AGE = int(EnvHelper.get('HSTS_MAX_AGE', 31536000))  # 1 year in seconds
HSTS_INCLUDE_SUBDOMAINS = EnvHelper.get('HSTS_INCLUDE_SUBDOMAINS', 'true').lower() == 'true'
HSTS_PRELOAD = EnvHelper.get('HSTS_PRELOAD', 'false').lower() == 'true'

# Referrer Policy (controls referrer information)
REFERRER_POLICY = EnvHelper.get('REFERRER_POLICY', 'strict-origin-when-cross-origin')

# Permissions Policy (formerly Feature Policy)
PERMISSIONS_POLICY = EnvHelper.get('PERMISSIONS_POLICY', None)  # None = use secure defaults