from django.contrib import admin
from myapp.models import Employee,Student, Product

# Register your models here.

admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Product)