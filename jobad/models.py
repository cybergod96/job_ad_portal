from django.db import models


class Employer(models.Model):
    company_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)


class Advertisement(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)


class ApplyForm(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    reply = models.CharField(max_length=255)
