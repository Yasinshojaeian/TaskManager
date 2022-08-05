from django.db import models
from django.contrib.auth.models import User
from extentions.Utils import jalali_converter
from extentions.check_value import limit_file_size
# Create your models here.

    
class Project(models.Model):
    STATUS_CHOICES = {
        (1, 'غیرفعال'),
        (2, 'فعال'),
        (3, 'رد شده'),
        (4, 'انجام شده'),
    }
    name = models.CharField(max_length=200,verbose_name='نام')
    description = models.TextField(verbose_name='توضیحات')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ پایان')
    experts = models.ManyToManyField(User,verbose_name='کارشناسان')
    image = models.ImageField(verbose_name='تصویر',validators=[limit_file_size],upload_to='Project')
    price = models.IntegerField(verbose_name='قیمت')
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,verbose_name='ایجاد کننده',null=True,related_name='creator',editable=False)
    status = models.IntegerField(choices=sorted(STATUS_CHOICES), default=1, verbose_name="وضعیت")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural ='پروژه ها'
    
    def jdate(self):
        return jalali_converter(self.date)