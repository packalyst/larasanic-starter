"""
Cache Configuration
Configure cache drivers and stores
"""
from larasanic.support.env_helper import env

# Default cache driver
# Options: 'file', 'redis'
CACHE_DRIVER = env('CACHE_DRIVER', 'file')

# Cache stores configuration
CACHE_STORES = {
    # File-based cache (default)
    'file': {
        'driver': 'file',
        'path': None,  # Uses Storage.cache_data() if None
    },

    # Redis cache (recommended for production)
    'redis': {
        'driver': 'redis',
        'url': env('REDIS_URL', 'redis://localhost:6379/0'),
    },
}

# Get the default store configuration
def get_default_store():
    """Get the default cache store configuration"""
    return CACHE_STORES.get(CACHE_DRIVER, CACHE_STORES['file'])
