from django.contrib import admin
from APP.models import Emp

#Register your models here.

class EmpAdmin(admin.ModelAdmin):
     list_display =('First_Name','Last_Name','Mobile_Number','Email_Id','Gender','Salary','Address')


admin.site.register(Emp, EmpAdmin)
