from django.shortcuts import render, redirect


def auth_user(func):
    def wrap(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('address:login')
    return wrap
