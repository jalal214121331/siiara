from django.db import models
import datetime
# Create your models here.

class Users(models.Model):
    username = models.CharField(verbose_name="اسم المستخدم", max_length=255)
    email = models.CharField(verbose_name="البريد الالكتروني", max_length=255)
    createDate = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.username