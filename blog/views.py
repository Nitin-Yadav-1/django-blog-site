from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_GET, require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import models, forms


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


@require_http_methods(['GET', 'POST'])
@login_required
def createBlog(request):
  if request.method == 'POST':
    form = forms.BlogCreationForm(request.POST)
    if form.is_valid():
      form.cleaned_data['user'] = request.user
      new_blog = form.save(commit=False)
      new_blog.author = request.user
      new_blog.save() 
      return redirect(reverse("blog", args=(new_blog.id,)))
  else:
    form = forms.BlogCreationForm()
  return render(request, 'create_blog.html', {'form' : form})


@require_http_methods(['GET', 'POST'])
@login_required
def updateBlog(request, id):
  try:
    blog = models.Blog.objects.get(id=id)
  except models.Blog.DoesNotExist:
    raise Http404('Blog does not exist.')
  
  if request.method == 'POST':
    form = forms.BlogUpdationForm(request.POST, instance=blog)
    if form.is_valid():
      form.save()
      return redirect(reverse('blog', args=(blog.id,)))
  else:
    form = forms.BlogUpdationForm(instance=blog)
  
  return render(request, 'update_blog.html', {'form' : form})