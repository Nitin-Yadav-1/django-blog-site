from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
from . import models


@require_GET
def allBlogs(request):
  blogs = models.Blog.objects.all()
  return render(request, 'all_blogs.html', {'blogs' : blogs})