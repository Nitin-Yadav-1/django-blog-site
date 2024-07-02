from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from . import forms


class CustomUserAdmin(UserAdmin):
  add_form = forms.CustomUserCreationForm
  form = forms.CustomUserChangeForm
  model = models.CustomUser
  list_display = ['username', 'email', 'profile_image_big', 'profile_image_small']


admin.site.register(models.CustomUser, CustomUserAdmin)