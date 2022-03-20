from functools import wraps
from django.core.exceptions import PermissionDenied

def ajax_login_required(view):
    """
        instead of redirecting to login page, return 403 when user is not authenticated
    """
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied
        return view(request, *args, **kwargs)
    return wrapper