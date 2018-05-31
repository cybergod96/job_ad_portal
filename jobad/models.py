from django.db import models
from django.contrib.auth.models import User


class Employer(models.Model):
    company_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name + ", " + self.branch


class Advertisement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class ApplyForm(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    reply = models.CharField(max_length=255)
