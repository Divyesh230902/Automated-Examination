from django.contrib import admin
from .models import Professor, Student, Department, Branch

# Register your models here.
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Branch)
