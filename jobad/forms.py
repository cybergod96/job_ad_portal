from django import forms


class AdvertisementApplyForm(forms.Form):
    answer = forms.CharField(max_length=512, widget=forms.Textarea)


class AddAdForm(forms.Form):
    name = forms.CharField(max_length=255, label=u"Tytuł")
    job_title = forms.CharField(max_length=255, label=u"Stanowisko")
    description = forms.CharField(max_length=512, label=u"Opis", widget=forms.Textarea)
