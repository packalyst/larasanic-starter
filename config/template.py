"""
Template & View Configuration
Centralized configuration for Blade template engine and view rendering
"""
from larasanic.support import EnvHelper

# ============================================================================
# Blade Template Engine Configuration
# ============================================================================

BLADE_ENGINE_CONFIG = {
    'cache_enabled': EnvHelper.get_bool('BLADE_CACHE_ENABLED', False),
    'cache_storage_type': EnvHelper.get('BLADE_CACHE_STORAGE', 'disk'), # 'disk' or 'memory'
    'cache_max_size': int(EnvHelper.get('BLADE_CACHE_MAX_SIZE', 1000)),
    'cache_ttl': int(EnvHelper.get('BLADE_CACHE_TTL', 3600)),  # seconds
    'track_mtime': EnvHelper.get_bool('BLADE_TRACK_MTIME', True),  # Auto-reload on file changes
    'file_extension': EnvHelper.get('BLADE_FILE_EXTENSION', '.html'), # '.html' or '.blade.php'
    'allow_python_blocks': EnvHelper.get_bool('BLADE_ALLOW_PYTHON', False),  # Security: disabled by default
}

# ============================================================================
# View Rendering Configuration
# ============================================================================
BLADE_VIEW_CONFIG = {
    'spa_enabled': EnvHelper.get_bool('BLADE_SPA_ENABLED', True),
    'spa_layout': EnvHelper.get('BLADE_SPA_LAYOUT', 'base'),
    'spa_content_variable': EnvHelper.get('BLADE_SPA_CONTENT_VAR', 'initial_content'), # Empty content, will be loaded via AJAX
    'spa_initial_path': EnvHelper.get('BLADE_SPA_INITIAL_PATH', 'initial_partial'),# Tell the client which partial to load
    'error_template_prefix': EnvHelper.get('BLADE_ERROR_PREFIX', 'errors'),
}

BLADE_ICONS = {
    'packages': {
        'tabler': {
            'outline': 'node_modules/@tabler/icons/icons/outline',
            'filled': 'node_modules/@tabler/icons/icons/filled'
        },
        'heroicons': {
            'outline': 'node_modules/heroicons/24/outline',
            'solid': 'node_modules/heroicons/24/solid'
        },
        'lucide': 'node_modules/lucide-static/icons',
        'feather': 'node_modules/feather-icons/dist/icons',
    },
    'fallback': '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="10"></circle>
    <line x1="12" y1="8" x2="12" y2="12"></line>
    <line x1="12" y1="16" x2="12.01" y2="16"></line>
</svg>
'''
}