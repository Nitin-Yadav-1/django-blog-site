from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET
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
  return render(request, 'profile.html', {"request_user" : user})

