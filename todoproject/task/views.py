from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import TaskCategoryForm, TaskForm
from .models import Task, TaskCategory

@login_required
def home_view(request):

    default_categories = TaskCategory.objects.filter(is_default=True)
    user_categories = TaskCategory.objects.filter(user=request.user, is_default=False)
    

    context = {
        "default_categories":default_categories,
        "user_categories":user_categories,
        
    }
    return render(request, "task/home.html", context)

@login_required
def list_tasks(request, category_id):
    category = get_object_or_404(TaskCategory, pk=category_id)
    tasks = Task.objects.filter(category=category, user=request.user)

    context = {
        "tasks":tasks,
        "category":category,
    }
    return render(request, "task/tasks.html", context)

@login_required
def add_task(request, category_id):
    category = get_object_or_404(TaskCategory, pk=category_id)
    user =request.user

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.category = category
            task.save()
            return redirect("task:home")
        
    form = TaskForm()
    context = {
        "form":form,
        "category": category,
    }
    return render(request, "task/add_task.html", context)

@login_required
def add_category(request):
    user =request.user

    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            task_category = form.save(commit=False)
            task_category.user = user
            task_category.save()
            return redirect("task:home")
        
    form = TaskCategoryForm()
    context = {
        "form":form,
    }
    return render(request, "task/add_category.html", context)

def detail_task(request):
    pass

def update_task(request):
    pass

def delete_task(request):
    pass