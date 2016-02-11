from __future__ import unicode_literals

from django.db import models


class Samin(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)

