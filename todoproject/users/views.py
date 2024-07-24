from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import UserRegistrationForm

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {
        "form":form,
    }
    return render(request, "users/register.html", context)