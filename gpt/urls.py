from django.contrib import admin
from django.urls import path, include
from gpt_site import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('', include('gpt_site.urls')),
    path('admin/', admin.site.urls),
]

