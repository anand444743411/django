from django.db import models


# Create your models here.


class Emp(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Mobile_Number = models.IntegerField()
    Email_Id = models.EmailField()
    Gender = models.CharField(max_length=30)
    Salary = models.IntegerField()
    Address = models.CharField(max_length=30)
