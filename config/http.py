"""
HTTP Client Configuration
Configure the HTTP client behavior and security settings
"""

# Security level: STRICT, BALANCED, or RELAXED
# STRICT: Maximum security, may break some sites
# BALANCED: Good security with compatibility (recommended)
# RELAXED: Minimal security for testing only
SECURITY_LEVEL = 'BALANCED'

# Default request timeout in seconds
TIMEOUT = 30

# Maximum retry attempts for failed requests
MAX_RETRIES = 1

# Verify SSL certificates
VERIFY_SSL = True

# Follow HTTP redirects
FOLLOW_REDIRECTS = True

# Maximum number of redirects to follow
MAX_REDIRECTS = 10

# HTTP proxy URL (None to disable)
# Example: 'http://proxy.example.com:8080'
PROXY = None

# Rate limiting: (max_requests, window_seconds)
# Example: (10, 60) = max 10 requests per 60 seconds
# None to disable rate limiting
RATE_LIMIT = None

# User agent string for requests
USER_AGENT = 'LaraSanic/1.0'

# Custom headers to include in all requests
CUSTOM_HEADERS = {
    # Add your custom headers here
    # 'X-API-Key': 'your-api-key',
}
