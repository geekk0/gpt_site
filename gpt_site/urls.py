from django.contrib import admin
from django.urls import path
from gpt_site import views

urlpatterns = [
    path('', views.main, name=''),
    path("logout", views.user_logout, name="logout"),
    path('get_gpt_response', views.get_gpt_response, name='get_gpt_response')
]