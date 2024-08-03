from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import TaskCategoryForm, TaskForm
from .models import Task, TaskCategory, UserPoints, Achievement, UserAchievement

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
            return redirect("task:category_tasks", category_id=category_id)
    else:
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
            return redirect(task_category.get_absolute_url())
    else:   
        form = TaskCategoryForm()

    context = {
        "form":form,
    }
    return render(request, "task/add_category.html", context)

@login_required
def category_detail(request, category_id):
    category = get_object_or_404(TaskCategory, id=category_id)
    context = {
        "category":category,
    }
    return render(request, "task/category_detail.html", context)

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(TaskCategory, id=category_id)
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(category.get_absolute_url())
    else:
        form = TaskCategoryForm(instance=category)
    
    context = {
        "form":form,
    }
    return render(request, "task/edit_category.html", context)

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(TaskCategory, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('task:home')
    
    context = {
        "category":category,
    }
    return render(request, "task/delete_category.html", context)

@login_required
def toggle_task_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    user_points, created = UserPoints.objects.get_or_create(user=request.user)
    
    if task.is_done:
        task.is_done = False
        user_points.points -= 1
    else:
        task.is_done = True
        user_points.points += 1
        

    task.save()
    user_points.save()

    # Check for achievements
    achievements = Achievement.objects.filter(points_required__lte=user_points.points)
    for achievement in achievements:
        UserAchievement.objects.get_or_create(user=request.user, achievement=achievement)

    return redirect('category_tasks', category_id=task.category.id)

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {
        "task":task,
    }
    return render(request, "task/task_detail.html", context)

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(task.get_absolute_url())
    else:
        form = TaskForm(instance=task)
    
    context = {
        "form":form,
        "task":task,
    }
    return render(request, "task/edit_task.html", context)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    category_id = task.category.id
    if request.method == 'POST':
        task.delete()
        return redirect("task:category_tasks", category_id=category_id)
    
    context = {
        "task":task,
    }
    return render(request, "task/delete_task.html", context)