from django.db import models

# Create your models here.

class Meeting(models.Model):
    date = models.DateField(verbose_name='تاریخ')
    subject = models.CharField(max_length=255,verbose_name='موضوع')
    solution = models.CharField(max_length=255,verbose_name='راه حل')
    
    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = 'جلسه'
        verbose_name_plural ='جلسات '