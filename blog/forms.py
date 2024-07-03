
from django.forms import ModelForm
from . import models


class BlogCreationForm(ModelForm):
  class Meta:
    model = models.Blog
    fields = ('title', 'content')


class BlogUpdationForm(ModelForm):
  class Meta:
    model = models.Blog
    fields = ('title', 'content')