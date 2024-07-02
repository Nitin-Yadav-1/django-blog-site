from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  PROFILE_IMAGE_BIG_SIZE = (300,300)
  PROFILE_IMAGE_SMALL_SIZE = (50,50)

  profile_image_big = models.ImageField(
    upload_to='profile_image/',
    default='profile_image/default_big.jpeg',
  )
  profile_image_small = models.ImageField(
    upload_to='profile_image/',
    default='profile_image/default_small.jpeg'
  )

  def __str__(self):
    return self.username