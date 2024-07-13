from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_GET, require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q
from . import models, forms


@require_GET
def allBlogs(request):
  searchQuery = request.GET.get('search')
  if searchQuery is None:
    blogs = models.Blog.objects.all()
  else:
    filters = (Q(title__icontains=searchQuery) 
                | 
              Q(content__icontains=searchQuery)
    )
    blogs = models.Blog.objects.filter(filters)
  paginator = Paginator(blogs, 10)
  page_obj = paginator.get_page(request.GET.get('page'))
  return render(request, 'all_blogs.html', {'page_obj': page_obj})


@require_GET
def blog(request, id):
  try:
    blog = models.Blog.objects.get(id=id)
  except models.Blog.DoesNotExist:
    raise Http404("This blog does not exist")
  comment_form = forms.CommentCreationForm()
  currUserLikesBlog = ((request.user.is_authenticated) 
                          and 
                      (request.user.liked_blogs_set.filter(id=blog.id).count() == 1))
  context = {
    'blog' : blog, 
    'comment_form' : comment_form,
    'currUserLikesBlog' : currUserLikesBlog,
  }
  return render(request, 'blog.html', context=context)


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


@require_GET
@login_required
def deleteBlog(request, id):
  try:
    blog = models.Blog.objects.get(id=id)
  except models.Blog.DoesNotExist:
    raise Http404('Blog does not exist.')
  
  blog.delete()
  return redirect('all-blogs')


@require_http_methods(['POST'])
@login_required
def createComment(request, blog_id):
  form = forms.CommentCreationForm(request.POST)
  if form.is_valid():
    models.Comment.objects.create(
      user=request.user,
      blog_id=blog_id,
      content=form.cleaned_data.get('content')
    )
  return redirect(reverse('blog', args=(blog_id,)))


@require_GET
@login_required
def deleteComment(request, id):
  try:
    comment = models.Comment.objects.get(id=id)
  except models.Comment.DoesNotExist:
    raise Http404('comment does not exist')
  blog_id = comment.blog.id
  comment.delete()
  return redirect(reverse("blog", args=(blog_id,)))


@require_http_methods(['POST'])
@login_required
def toggleBlogLike(request, blog_id):
  try:
    blog = models.Blog.objects.get(id=blog_id)
  except models.Blog.DoesNotExist:
    raise Http404("Blog does not exist.")
  
  currUserDoesLike = len(blog.likes.filter(id=request.user.id)) > 0
  if currUserDoesLike:
    blog.likes.remove(request.user)
  else:
    blog.likes.add(request.user)

  return redirect(reverse('blog', args=(blog_id,)))
