from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
from django.http import Http404
from . import models


@require_GET
def allBlogs(request):
  blogs = models.Blog.objects.all()
  return render(request, 'all_blogs.html', {'blogs' : blogs})


@require_GET
def blog(request, id):
  try:
    blog = models.Blog.objects.get(id=id)
  except models.Blog.DoesNotExist:
    raise Http404("This blog does not exist")
  return render(request, 'blog.html', {'blog' : blog})