from django.db import models
from accounts.models import CustomUser


class Blog(models.Model):
  title = models.CharField(max_length=200, unique=True)
  content = models.TextField(max_length=5000)
  created_at = models.DateField(auto_now_add=True)
  last_updated_at = models.DateField(auto_now=True)
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  likes = models.ManyToManyField(CustomUser, related_name='liked_blogs_set')

  class Meta:
    ordering = ['-created_at', '-last_updated_at']

  def __str__(self):
    return self.title[:20] if len(self.title) <= 20 else f"{self.title[:10]}...{self.title[-10:]}"


class Comment(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
  content = models.CharField(max_length=500)


