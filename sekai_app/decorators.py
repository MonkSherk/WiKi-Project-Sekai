from django.shortcuts import redirect
from functools import wraps

from sekai_pj.settings import ADMIN_TOKEN


def admin_token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        token = request.COOKIES.get('admin_token')
        if token == ADMIN_TOKEN:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('admin_access_check')
    return _wrapped_view
