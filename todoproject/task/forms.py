from django import forms
from .models import Task, TaskCategory


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating Task instances.
    """
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "due_date",
            "time_spent",
            "priority_level",
            "is_done"
        ]

class TaskCategoryForm(forms.ModelForm):
    """
    Form for creating and updating TaskCategory instances.
    """
    class Meta:
        model = TaskCategory
        fields = [
            "name",
        ]
