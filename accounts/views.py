from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from . import forms


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