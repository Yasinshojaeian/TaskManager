from django.db import models
from Project.models import Project
from django.contrib.auth.models import User
# Create your models here.
class Financial(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,verbose_name='پروژه')
    price = models.IntegerField(verbose_name='قیمت')
    reciver = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='دریافت کننده')
    payer = models.ForeignKey(User, related_name='payer' ,on_delete=models.CASCADE,verbose_name='پرداخت کننده')
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator_financial')
    
    def __str__(self): 
        return self.project.name
    class Meta:
        verbose_name = 'مالی'
        verbose_name_plural ='مالی ها'