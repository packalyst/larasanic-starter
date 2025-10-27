"""
Web Routes
Routes for the web interface (HTML pages)
These routes automatically get 'web' middleware group applied
"""
from larasanic.support.facades import Route, Auth
from larasanic.http import ResponseHelper

# Favicon route
Route.get('/favicon.ico', lambda request: ResponseHelper.empty(status=200)).name('favicon')

# Home route - redirects based on auth status
async def home_handler(request):
    """
    Smart home route - redirects to appropriate page based on auth status
    """
    try:
        user = await Auth.get_user_from_request(request)
        if user:
            # User is authenticated - redirect to dashboard
            return ResponseHelper.redirect('/dashboard')
        else:
            # User is guest - redirect to login
            return ResponseHelper.redirect('/welcome')
    except Exception:
        # Error getting user - treat as guest
        return ResponseHelper.redirect('/login')

Route.get('/', home_handler).name('home')

# ============================================================================
# Guest Routes (Only for non-authenticated users)
# ============================================================================

Route.middleware(['guest', 'spa']).group(lambda: [
    Route.view('/login', 'pages.login').name('login'),
    Route.view('/register', 'pages.register').name('register'),
    Route.view('/welcome', 'pages.welcome').name('welcome'),
])

# ============================================================================
# Authenticated Routes (Require login)
# ============================================================================

Route.middleware(['auth', 'spa']).group(lambda: [
    Route.view('/dashboard', 'pages.dashboard').name('dashboard'),

])