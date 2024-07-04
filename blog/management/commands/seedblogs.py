from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from blog.models import Blog, Comment
import json, os, random


class Command(BaseCommand):
  help = "Adds fake blogs, comments and likes to the database"


  def handle(self, *args, **options):
    self.createFakeBlogs()
    self.createFakeComments()
    self.createFakeLikes()


  def createFakeBlogs(self):
    fakeBlogsDataFilePath = os.path.join(os.path.dirname(__file__), 'fake_blogs.json')
    with open(fakeBlogsDataFilePath) as file:
      fakeBlogData = json.load(file)
    users = list(CustomUser.objects.all())
    created_blogs_count = 0
    print("Creating fake blogs...")
    for fakeBlog in fakeBlogData:
      try:
        Blog.objects.create(
          title = fakeBlog['title'],
          content = fakeBlog['content'],
          author = users[random.randint(0, len(users)-1)]
        )
        created_blogs_count += 1
      except:
        pass
    print(f"{created_blogs_count} blogs created successfully")


  def createFakeComments(self):
    fakeCommentsDataFilePath = os.path.join(os.path.dirname(__file__), 'fake_comments.json')
    with open(fakeCommentsDataFilePath) as file:
      fakeCommentData = json.load(file)
    created_comments_count = 0
    blogs = list(Blog.objects.all())
    users = list(CustomUser.objects.all())
    print("Creating fake comments...")
    for fakeComment in fakeCommentData:
      try:
        Comment.objects.create(
          content = fakeComment['content'],
          user = users[random.randint(0, len(users)-1)],
          blog = blogs[random.randint(0, len(blogs)-1)]
        )
        created_comments_count += 1
      except:
        pass
    print(f"{created_comments_count} comments created successfully")


  def createFakeLikes(self):
    created_like_count = 0
    users = list(CustomUser.objects.all())    
    blogs = list(Blog.objects.all())
    print("Creating fake likes...")
    for blog in blogs:
      randomSelectedUsers = random.choices(users, k=random.randint(0, len(users)//2))
      for user in randomSelectedUsers:
        try:
          blog.likes.add(user)
          created_like_count += 1
        except:
          pass
    print(f"{created_like_count} likes created successfully")
    


