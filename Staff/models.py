from datetime import date
from operator import truediv
from pyexpat import model
from turtle import position
from unicodedata import name
from xml.dom import NO_MODIFICATION_ALLOWED_ERR
from django.db import models
from django.forms import CharField


class staff(models.Model):
    NO_IC            = models.AutoField(primary_key=True)
    First_name       = models.CharField(max_length=20)
    Last_namee       = models.CharField(max_length=20)
    staff_id         = models.IntegerField(null=True)
    nickname         = models.CharField(max_length=50)
    Gender           = models.CharField(max_length=10)
    Phone_no         = models.IntegerField(null=True)
    Email_address    = models.CharField(max_length=20)
    birth_ofDate     = models.DateField()
    Age              = models.IntegerField()
    Country          = models.CharField(max_length=20)
    City             = models.CharField(max_length=20)
    Salary           = models.IntegerField(null=True)
    Factory_no       = models.IntegerField(null=True)
    Badge_id         = models.IntegerField(null=True)
    Position         = models.CharField(max_length=20)
    Date_join        = models.DateTimeField()
    Reporting_to     = models.CharField(max_length=20)

    def __str__(self):
        return str(self.NO_IC)