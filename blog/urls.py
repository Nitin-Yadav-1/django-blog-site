from django.urls import path
from . import views

urlpatterns = [
  path("all/", views.allBlogs, name='all-blogs'),
  path("<int:id>/", views.blog, name='blog'),
  path("create/", views.createBlog, name='create-blog'),
  path("update/<int:id>/", views.updateBlog, name='update-blog'),
  path("delete/<int:id>/", views.deleteBlog, name='delete-blog'),
  path("createComment/<int:blog_id>/", views.createComment, name='create-comment'),
  path("deleteComment/<int:id>/", views.deleteComment, name='delete-comment'),
  path("likeBlog/<int:blog_id>/", views.toggleBlogLike, name='like-blog'),
]