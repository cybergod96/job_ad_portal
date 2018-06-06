"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User

from .models import Employer

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    company_name = forms.CharField(max_length=255)
    branch = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data["username"],
                                        email=self.cleaned_data["email"],
                                        password=self.cleaned_data["password"])
        user.save()

        employer = Employer.objects.create(user=user,
                                          company_name=self.cleaned_data["company_name"],
                                          branch=self.cleaned_data["branch"])
        employer.save()



        return employer


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())

class NewAdvertisment(forms.Form):
    name = forms.CharField(label='Nazwa ogłoszenia', max_length=255)
    job_title = forms.CharField(label='Praca', max_length=255)

class AdvertisementApplyForm(forms.Form):
    answer = forms.CharField(max_length=512, widget=forms.Textarea)


class AddAdForm(forms.Form):
    name = forms.CharField(max_length=255, label=u"Tytuł")
    job_title = forms.CharField(max_length=255, label=u"Stanowisko")
    description = forms.CharField(max_length=512, label=u"Opis", widget=forms.Textarea)
