from django.urls import path
from . import views

urlpatterns = [
  path("all/", views.allBlogs, name='all-blogs'),
  path("<int:id>/", views.blog, name='blog'),
  path("create/", views.createBlog, name='create-blog'),
]