from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from API import urls


@login_required(login_url='login')
def list(request):
    return render(request, 'frontend/main.html')