from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    description = models.TextField(verbose_name='توضیحات')
    create_date = models.DateField(auto_now_add=True)
    expert = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کارشناس')
    voice = models.FileField(upload_to='voice', verbose_name='توضیحات صوتی',null=True,blank=True)
    possible_time = models.TimeField(verbose_name='زمان تخمینی ')
    main_time = models.TimeField(verbose_name='زمان حساب شده ')
    creator = models.ForeignKey(User, on_delete=models.CASCADE,editable=False,related_name='creator_task')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'تسک'
        verbose_name_plural ='تسک ها'