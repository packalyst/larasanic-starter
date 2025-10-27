"""
API Routes
RESTful API endpoints (JSON responses)
These routes automatically get 'api' middleware group applied
"""
from larasanic.support.facades import Route, App
from larasanic.http import ResponseHelper

# ============================================================================
# API Status & Health
# ============================================================================

async def api_status(request):
    return ResponseHelper.success({
        'status': 'ok',
        'version': '1.0',
        'blueprint': 'api'
    })

Route.get('/status', api_status).name('status')

# ============================================================================
# API Catch-All (MUST BE LAST!)
# ============================================================================
# Catches any /api/* route that doesn't match above and returns proper JSON 404
# This prevents API routes from falling through to the SPA catch-all
Route.any('/<path:path>',
    lambda request, path='': ResponseHelper.error(
        f'API endpoint not found: /{path}',
        status=404
    )
).name('api.not_found')