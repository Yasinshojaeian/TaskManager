from django.db import models

# Create your models here.

class Ideas(models.Model):
    name = models.CharField(max_length=255 , verbose_name='نام')
    description = models.TextField(verbose_name='توضیحات')
    voice = models.FileField(upload_to='ideas')
    class Meta:
        verbose_name = 'ایده'
        verbose_name_plural ='ایده ها'