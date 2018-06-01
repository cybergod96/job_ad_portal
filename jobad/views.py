from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from .models import Advertisement


def index(request):
    return render(request, 'jobad/home.html', {"ads": Advertisement.objects.all()})


def viewad(request, ad_id):
    return render(request, 'jobad/viewad.html', {"ad": Advertisement.objects.get(pk=ad_id)})


def appply(request, ad_id):
    return render(request, "jobad/apply.html", {"ad": Advertisement.objects.get(pk=ad_id)})


def register(request):
    return render(request, "jobad/register.html")


def login(request):
    return render(request, "jobad/login.html")


def account(request):
    return render(request, "jobad/account.html")


def logout_view(request):
    logout(request)
    return render(request, 'jobad/home.html', {"ads": Advertisement.objects.all()})


@login_required
def add_ad(request):
    return render(request, 'jobad/addad.html')
