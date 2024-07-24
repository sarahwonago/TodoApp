from django.urls import path
from .views import logout_view, register_view

app_name = "users"

urlpatterns = [
    path("logout-user/", logout_view, name="logout-user"),
    path("register/", register_view, name="register"),
]