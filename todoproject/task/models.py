from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskCategory(models.Model):
    class Meta:
        verbose_name_plural = "TaskCategories"

    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        verbose_name_plural = "Tasks"

    priority_choices = (
            ("L", "LOW"),
            ("H", "HIGH"),
            ("M", "MEDIUM")
        )

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(TaskCategory, related_name="tasks", on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    time_spent = models.IntegerField()
    priority_level =  models.CharField(choices=priority_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Achievement(models.Model):
    class Meta:
        verbose_name_plural = "Achievements"

    name = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField()
    badge = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class UserAchievement(models.Model):
    class Meta:
        verbose_name_plural = "UserAchievements"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date_achieved = models.DateTimeField(auto_now_add=True)

class UserPoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)


    