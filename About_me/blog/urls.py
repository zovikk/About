from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.post_view, name="post-list"),
    path('Add/', views.create, name="add-post"),
    path('like', views.like_post, name="like-post"),
]
