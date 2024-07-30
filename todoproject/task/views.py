from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

@login_required
def home_view(request):
    return render(request, "task/home.html")

class HomeView(TemplateView):
    template_name = "task/home.html"


def create_task(request):
    pass

def detail_task(request):
    pass

def update_task(request):
    pass

def delete_task(request):
    pass