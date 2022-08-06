from django.db import models
from Project.models import Project

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=80 , verbose_name='نام')
    priority = models.IntegerField(default=1, verbose_name='اولویت')
    project = models.ForeignKey(Project,on_delete=models.CASCADE , verbose_name='پروژه')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural ='دسته بندی ها'