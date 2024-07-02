from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

class CustomUser(AbstractUser):
  PROFILE_IMAGE_SIZE = (300,300)

  profile_image = ResizedImageField(
    upload_to='profile_image/',
    default='profile_image/default.jpeg',
    blank=True,
    size=PROFILE_IMAGE_SIZE,
    keep_meta=False
  )

  def __str__(self):
    return self.username
  