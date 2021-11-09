from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ToDo)
admin.site.register(ToMeet)
admin.site.register(MonthGoal)
admin.site.register(Habit)
