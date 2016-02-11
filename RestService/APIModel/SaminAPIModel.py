from django.db import models


class Samin(models.Model):


    Firstname = models.CharField(max_length=50)
    Lastname  = models.CharField(max_length=50)
    Email     = models.EmailField()
    Address   = models.CharField(max_length=100)

