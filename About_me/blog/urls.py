from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog),
    path('Add/', views.create),
]
