from django.contrib import admin

from Project.models import Project
from jalali_date.admin import ModelAdminJalaliMixin

# Register your models here.
class ProjectAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    fields = ('name','description','image','experts','start_date','end_date','price','status')
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Project,ProjectAdmin)