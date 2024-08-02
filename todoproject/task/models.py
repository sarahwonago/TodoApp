from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskCategory(models.Model):
    class Meta:
        verbose_name_plural = "TaskCategories"

    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="task_categories", on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        verbose_name_plural = "Tasks"

    PRIORITY_LOW = 'L'
    PRIORITY_MEDIUM = 'M'
    PRIORITY_HIGH = 'H'
    PRIORITY_CHOICES = (
            (PRIORITY_LOW, "Low"),
            (PRIORITY_MEDIUM, "Medium"),
            (PRIORITY_HIGH, "High")
        )

    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(TaskCategory, related_name="tasks", on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    time_spent = models.PositiveIntegerField()
    priority_level =  models.CharField(choices=PRIORITY_CHOICES, max_length=1)
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
    points = models.PositiveIntegerField()
    badge = models.ImageField(blank=True, null=True, upload_to='badges/')

    def __str__(self):
        return self.name
    
class UserAchievement(models.Model):
    class Meta:
        verbose_name_plural = "User Achievements"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date_achieved = models.DateTimeField(auto_now_add=True)


class UserPoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)
    
    def add_points(self, point):
        self.points += point
        self.save()

    def subtact_points(self, point):
        self.points -= point
        self.save()