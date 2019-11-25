from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class Details(AbstractUser):
    # first_name = models.CharField(max_length=150)
    # last_name = models.CharField(max_length=150)
    # email = models.EmailField()
    phonenumber = models.BigIntegerField(null=True)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    # password = models.CharField(max_length=100)
    # password1 = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'app2_details'

    # def __str__(self):
    #     return self.first_name + '_' + self.last_name

