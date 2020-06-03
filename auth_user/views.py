from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout



def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
