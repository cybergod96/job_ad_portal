from django.contrib import admin
from .models import Advertisement, Employer, ApplyForm, AdvertisementReply

admin.site.register(Advertisement)
admin.site.register(Employer)
admin.site.register(ApplyForm)
admin.site.register(AdvertisementReply)