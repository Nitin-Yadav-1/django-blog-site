from django.core.management.base import BaseCommand
from accounts.models import CustomUser
import json, os

class Command(BaseCommand):
  help = "Adds fake users to the database"

  def handle(self, *args, **options):
    fakeUsersDataFilePath = os.path.join(os.path.dirname(__file__), 'fake_users.json')
    with open(fakeUsersDataFilePath) as file:
      data = json.load(file)

    createdCount = 0

    print('Adding fake users....')
    for user in data:
      try:
        CustomUser.objects.create_user(
          first_name = user['first_name'],
          last_name = user['last_name'],
          username = user['username'],
          email = user['email'],
          password = 'pass@1234',
        )
        createdCount += 1
      except:
        pass

    print(f'{createdCount} users created successfully')