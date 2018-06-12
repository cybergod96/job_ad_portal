"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User

from .models import Employer, Advertisement, ApplyForm, AdvertisementReply


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, label=u"Nazwa użytkownika")
    email = forms.CharField(max_length=255, label=u"E-mail")
    company_name = forms.CharField(max_length=255, label="Nazwa firmy")
    branch = forms.CharField(max_length=255, label="Branża")
    password = forms.CharField(widget=forms.PasswordInput(), label="Hasło")

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
    username = forms.CharField(max_length=255, label="Nazwa użytkownka")
    password = forms.CharField(widget=forms.PasswordInput(), label="Hasło")


class AdvertisementApplyForm(forms.Form):
    fields_number = 0
    def add_fields(self, ad_id):
        fields_dict = eval(ApplyForm.objects.get(advertisement_id=ad_id).content)
        self.fields_number = int(fields_dict['fields_number'])
        for i in range(1, self.fields_number + 1):
            field = fields_dict['field_%d' % i]
            if field['type'] == "text":
                self.fields['field_%d' % i] = forms.CharField(label=field['label'])
            elif field['type'] == "textarea":
                self.fields['field_%d' % i] = forms.CharField(label=field['label'], widget=forms.Textarea)
            elif field['type'] == "number":
                self.fields['field_%d' % i] = forms.IntegerField(label=field['label'])



class AddAdForm(forms.Form):
    name = forms.CharField(max_length=255, label=u"Tytuł")
    job_title = forms.CharField(max_length=255, label=u"Stanowisko")
    description = forms.CharField(max_length=512, label=u"Opis", widget=forms.Textarea)

class FilterForm(forms.Form):
    company_name = forms.CharField(max_length=255, label=u"Nazwa firmy")
    job_title = forms.CharField(max_length=255, label=u"Stanowisko")
    branch = forms.CharField(max_length=255, label="Branża")