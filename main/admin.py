from django.contrib import admin
from .models import Evaluator, Measure, Objective, Rubric
from django.contrib.auth.models import Group


# Modify the view of Evaluator
class EvaluatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')


# Register your models here.
admin.site.register(Evaluator, EvaluatorAdmin)
admin.site.register(Measure)
admin.site.register(Objective)
admin.site.register(Rubric)

# Unregister groups that are not needed
admin.site.unregister(Group)

# Change header
admin.site.site_header = "Admin Dashboard"