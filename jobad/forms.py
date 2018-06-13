"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User

from .models import Employer, Advertisement, ApplyForm, AdvertisementReply


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, label=u"Nazwa użytkownika",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nazwa użytkownika'}))
    email = forms.CharField(max_length=255, label=u"E-mail",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail'}))
    company_name = forms.CharField(max_length=255, label="Nazwa firmy",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nazwa firmy'}))
    branch = forms.CharField(max_length=255, label="Branża",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Branża'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Hasło'}), label="Hasło")

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
    username = forms.CharField(max_length=255, label="Nazwa użytkownka",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nazwa użytkownika'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Hasło'}), label="Hasło")


class AdvertisementApplyForm(forms.Form):
    fields_number = 0
    def add_fields(self, ad_id):
        fields_dict = eval(ApplyForm.objects.get(advertisement_id=ad_id).content)
        self.fields_number = int(fields_dict['fields_number'])
        for i in range(1, self.fields_number + 1):
            field = fields_dict['field_%d' % i]
            if field['type'] == "text":
                self.fields['field_%d' % i] = forms.CharField(label=field['label'],widget=forms.TextInput(attrs={'class':'form-control'}) )
            elif field['type'] == "textarea":
                self.fields['field_%d' % i] = forms.CharField(label=field['label'], widget=forms.Textarea(attrs={'class':'form-control'}))
            elif field['type'] == "number":
                self.fields['field_%d' % i] = forms.IntegerField(label=field['label'], widget=forms.NumberInput(attrs={'class':'form-control'}))



class AddAdForm(forms.Form):
    name = forms.CharField(max_length=255, label=u"Tytuł", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tytuł'}))
    job_title = forms.CharField(max_length=255, label=u"Stanowisko", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Stanowisko'}))
    description = forms.CharField(max_length=512, label=u"Opis", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Opis'}))
