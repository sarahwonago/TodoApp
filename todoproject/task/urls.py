from django.urls import path
from .views import home_view, list_tasks, add_task, add_category

app_name="task"

urlpatterns = [
    path("", home_view, name="home"),
    path("categories/tasks/<int:category_id>/", list_tasks, name="category_tasks"),
    path("category/add-task/<int:category_id>/", add_task, name="add_task"),
    path("add-category/", add_category, name="add_category"),
]