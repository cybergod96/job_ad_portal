from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from .filters import AdFilter

from .models import Advertisement, Employer, ApplyForm
from .forms import AddAdForm, LoginForm, RegisterForm, AdvertisementApplyForm, AdvertisementReply

import json

from django.utils.html import format_html


def index(request):
    return render(request, 'jobad/home.html', {"ads": Advertisement.objects.all()})


def viewad(request, ad_id):
    return render(request, 'jobad/viewad.html', {"ad": Advertisement.objects.get(pk=ad_id)})


@csrf_protect
def apply(request, ad_id):
    if request.method == 'POST':
        form = AdvertisementApplyForm(request.POST)
        form.add_fields(ad_id)
        if form.is_valid():
            reply = AdvertisementReply.objects.create(advertisement_id=ad_id)
            reply.advertisement = Advertisement.objects.get(pk=ad_id)
            reply_dict = dict()
            for i in range(1, form.fields_number + 1):
                reply_dict[i] = {"label": form.fields['field_%d' % i].label,
                                 "value": form.cleaned_data['field_%d' % i]
                                 }
            reply.content = json.dumps(reply_dict, ensure_ascii=False)
            reply.save()
            return redirect('jobad:index')
    else:
        form = AdvertisementApplyForm()
        form.add_fields(ad_id)

    return render(request, "jobad/apply.html", {"ad": Advertisement.objects.get(pk=ad_id),
                                                "form": form})


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                auth.login(request, user)
                return render(request, "jobad/home.html")
            else:
                return HttpResponse('blad logowania')

    else:
        form = RegisterForm()

    return render(request, 'jobad/register.html', {'form': form})


def search(request):
    query = AdFilter(request.GET, queryset=Advertisement.objects.all())
    return render(request, 'jobad/filter.html', {'ads': query})


@csrf_protect
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                auth.login(request, user)
                return redirect('jobad:account')
            else:
                return HttpResponse('blad logowania')
        else:
            return HttpResponse('not valid')

    else:
        form = LoginForm()

    return render(request, 'jobad/login.html', {'form': form})


def account(request):
    ads = Advertisement.objects.filter(employer__user=request.user)
    return render(request, "jobad/account.html", {"ads": ads})


def logout_view(request):
    logout(request)
    # return render(request, 'jobad/home.html', {"ads": Advertisement.objects.all()})
    return redirect('jobad:index')


@login_required
def add_ad(request):
    if request.method == 'POST':
        form = AddAdForm(request.POST)
        if form.is_valid():
            ad = Advertisement.objects.create(employer=Employer.objects.get(user=request.user))
            ad.name = form.cleaned_data["name"]
            ad.job_title = form.cleaned_data["job_title"]
            ad.description = form.cleaned_data["description"]

            num = int(request.POST['additional_fields_number'])
            custom_fields = dict()
            custom_fields['fields_number'] = num
            for i in range(1, num + 1):
                custom_fields['field_%d' % i] = {"label": request.POST['field%d_label' % i],
                                                 "type": request.POST['field%d_type' % i]}
            apply_form = ApplyForm.objects.create(advertisement=ad)
            apply_form.content = json.dumps(custom_fields, ensure_ascii=False)

            ad.save()
            apply_form.save()
            return redirect('jobad:account')
    else:
        form = AddAdForm()
    return render(request, 'jobad/addad.html', {"form": form})


@login_required
def edit_ad(request, ad_id):
    if request.method == 'POST':
        ad_form = AddAdForm(request.POST)
        if ad_form.is_valid():
            ad = Advertisement.objects.get(pk=ad_id)
            af = ApplyForm.objects.get(advertisement_id=ad_id)

            ad.name = ad_form.cleaned_data['name']
            ad.job_title = ad_form.cleaned_data['job_title']
            ad.description = ad_form.cleaned_data['description']
            ad.save()

            num = int(request.POST['additional_fields_number'])
            custom_fields = dict()
            custom_fields['fields_number'] = num
            for i in range(1, num + 1):
                custom_fields['field_%d' % i] = {"label": request.POST['field%d_label' % i],
                                                 "type": request.POST['field%d_type' % i]}
            af.content = json.dumps(custom_fields, ensure_ascii=False)
            af.save()
            return redirect('jobad:account')
    else:
        form_data = eval(ApplyForm.objects.get(advertisement_id=ad_id).content)
        fields_num = form_data['fields_number']
        fields_content = ""
        ad = Advertisement.objects.get(pk=ad_id)
        ad_form = AddAdForm()
        ad_form.fill(ad.name, ad.job_title, ad.description)
        for i in range(1, fields_num + 1):
            sel_text = "selected" if form_data['field_%d' % i]['type'] == "text" else ""
            sel_textarea = "selected" if form_data['field_%d' % i]['type'] == "textarea" else ""
            sel_number = "selected" if form_data['field_%d' % i]['type'] == "number" else ""
            fields_content += """ <div id="div_field_%d" class="field_box">
            <label for="fileld%d_label" id="label_%d" class="field_box_label">Etykieta: </label>
            <input type="text" name="field%d_label" id="txt_%d" class="field_box_textarea" value="%s">
            <label for="field%d_type" id="label2_%d" class="field_box_label">Typ: </label>         
            <select name="field%d_type" id="select_%d" class="field_box_select">
            <option value="text" %s>Pole tekstowe</option>
            <option value="textarea" %s>Pole tekstowe (długie)</option>
            <option value="textnumber" %s>Liczba</option>
            </select>
            
            </div>""" % (
            i, i, i, i, i, form_data['field_%d' % i]['label'], i, i, i, i, sel_text, sel_textarea, sel_number)
    return render(request, 'jobad/editad.html', {"additional_fields_number": fields_num,
                                                 "additional_fields": format_html(fields_content),
                                                 "form": ad_form,
                                                 "hidden":  format_html("""<input type="hidden" value="%d" id="additional_fields_number" name="additional_fields_number">""" % fields_num),
                                                 "jstest": "Hadas"})


@login_required
def remove_ad(request, ad_id):
    Advertisement.objects.filter(pk=ad_id).delete()
    return redirect('jobad:account')


@login_required
def view_replies(request, ad_id):
    replies = AdvertisementReply.objects.filter(advertisement_id=ad_id)
    return render(request, 'jobad/replies.html', {"replies": replies})
