from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    ads = dict()
    return render(request, 'jobad/home.html', ads)


def viewad(request, ad_id):
    return HttpResponse(request, "Not implemented yet.")


def appply(request, ad_id):
    return HttpResponse(request, "Not implemented yet.")


def register(request):
    return HttpResponse(request, "Not implemented yet.")


def login(request):
    return HttpResponse(request, "Not implemented yet.")