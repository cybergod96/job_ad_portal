from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .models import Advertisement
from . import forms

def index(request):
    return render(request, 'jobad/home.html', {"ads": Advertisement.objects.all()})


def viewad(request, ad_id):
    return render(request, 'jobad/viewad.html', {"ad": Advertisement.objects.get(pk=ad_id)})


def appply(request, ad_id):
    return render(request, "jobad/apply.html", {"ad": Advertisement.objects.get(pk=ad_id)})


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                auth.login(request, user)
                return render(request, "jobad/home.html")
            else:
                return HttpResponse('blad logowania')

    else:
        form = forms.RegisterForm()

    return render(request, 'jobad/register.html', {'form': form})


@csrf_protect
def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                auth.login(request, user)
                return render(request, "jobad/home.html")
            else:
                return HttpResponse('blad logowania')

    else:
        form = forms.LoginForm()

    return render(request, 'jobad/login.html', {'form': form})


def account(request):
    return render(request, "jobad/account.html")


def logout_view(request):
    logout(request)
    return render(request, 'jobad/home.html', {"ads": Advertisement.objects.all()})


@login_required
def add_ad(request):
    return render(request, 'jobad/addad.html')
