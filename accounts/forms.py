from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = models.CustomUser
    fields = ("username", "email", "profile_image")


class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = models.CustomUser
    fields = ("username", "first_name", "last_name", "email", "profile_image")