from django.http import HttpResponse
from django.shortcuts import redirect


# this fnc means that authenticated(user which is logged in) user can not open the page
 # above which this decorator is used
def authenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

# This function opens the user home page directly if the user isn't logged out
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('userhome')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func