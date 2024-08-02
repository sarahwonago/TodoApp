from django.contrib import admin
from .models import Task, Achievement, TaskCategory, UserAchievement, UserPoints

admin.site.register(Task)
admin.site.register(Achievement)
admin.site.register(TaskCategory)
admin.site.register(UserAchievement)
admin.site.register(UserPoints)