from django.db import models
from django.contrib.auth.models import User

from django.utils.html import format_html

import json


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name + ", " + self.branch


class Advertisement(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class ApplyForm(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)


class AdvertisementReply(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    content = models.CharField(max_length=2048)

    def __str__(self):
        if len(self.content) > 32:
            return self.content[:32] + "..."
        else:
            return self.content

    def get_html(self):
        html = ""
        d = eval(self.content)
        for key in d:
            html += "<h3>" + str(d[key]['label']) + ":</h3><br>" + "<textarea class='form-control' rows='5' id='comment' readonly background:white>" + str(d[key]['value']) +"</textarea>"
            html += "<br>"
        return format_html(html)

