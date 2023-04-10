from django.db import models

# Create your models here.

class mubashir_studio(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=250)
    address = models.TextField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
