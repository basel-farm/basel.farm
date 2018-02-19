from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect

def logout(request):
    if request.user:
        django_logout(request)
    return redirect('login')
