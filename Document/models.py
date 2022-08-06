from django.db import models
from django.contrib.auth.models import User

class Documents(models.Model):
    name = models.CharField(max_length=255 , verbose_name='نام')
    files = models.FileField(verbose_name='سند')
    creator = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'سند'
        verbose_name_plural ='اسناد'