"""
Session Configuration
Laravel-style session management settings
"""
from larasanic.support import EnvHelper

# Session Driver
# Supported: "file", "cookie", "array", "cache"
DRIVER = EnvHelper.get('SESSION_DRIVER', 'file')

# Session Lifetime (in seconds)
LIFETIME = EnvHelper.get_int('SESSION_LIFETIME', 7200)  # 2 hours

# Session Cookie Name
COOKIE_NAME = EnvHelper.get('SESSION_COOKIE', 'framework_session')

# Cookie Path
COOKIE_PATH = '/'

# Cookie Domain
COOKIE_DOMAIN = EnvHelper.get('SESSION_DOMAIN', None)

# Cookie Security
COOKIE_SECURE = EnvHelper.get_bool('SESSION_SECURE_COOKIE', False)
COOKIE_HTTP_ONLY = True
COOKIE_SAME_SITE = 'Lax'  # 'Strict', 'Lax', 'None'

# Encrypt Session Data (for cookie driver)
ENCRYPT = True

# Session ID Regeneration
# Regenerate session ID on login to prevent fixation attacks
REGENERATE_ON_LOGIN = True

# Session Lottery (Garbage Collection)
# Probability: [2, 100] means 2% chance
SESSION_LOTTERY = [2, 100]

# Session Table (for database driver - future)
SESSION_TABLE = 'sessions'

# Session Store (for cache driver)
SESSION_STORE = None  # Uses default cache store
