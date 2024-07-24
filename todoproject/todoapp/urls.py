
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    #auth app for user authentication
    path("accounts/", include('django.contrib.auth.urls')),

    #custom-app urls
    path("", include('task.urls')),
    path("accounts/", include('users.urls')),
]
