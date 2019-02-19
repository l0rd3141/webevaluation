from django.contrib import admin
from .models import Evaluator, Measure, Objective, Student, StudentList
from django.contrib.auth.models import Group


# Modify the view of Evaluator
class EvaluatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'evaluation_status', 'evaluation_score']
    list_editable = ['evaluation_status']


# Register your models here.
admin.site.register(Evaluator, EvaluatorAdmin)
admin.site.register(Measure)
admin.site.register(Objective)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentList)


# Unregister groups that are not needed
admin.site.unregister(Group)

# Change header
admin.site.site_header = "Admin Dashboard"