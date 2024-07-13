from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import forms, models


@require_http_methods(['GET', 'POST'])
def signup(request):
  if request.method == 'POST':
    form = forms.CustomUserCreationForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = forms.CustomUserCreationForm()
  return render(request, 'registration/signup.html', {'form': form})


@require_GET
def profile(request, id):
  user = models.CustomUser.objects.get(id=id)
  if user is None:
    raise Http404('User does not exist.')
  blogsByUser = user.blog_set.all()
  return render(request, 'profile.html', {"request_user" : user, 'blogsByUser' : blogsByUser})


@require_GET
@login_required
def deleteAccount(request):
  user = request.user
  user.delete()
  return redirect('home')


@require_http_methods(['GET', 'POST'])
@login_required
def updateAccount(request):
  if request.method == 'POST':
    form = forms.CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect(
        reverse('profile', args = (request.user.id,))
      )
  else:
    form = forms.CustomUserChangeForm(instance=request.user)
  return render(request, 'update_account.html', {'form' : form})
