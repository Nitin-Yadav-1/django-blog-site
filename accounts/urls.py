from django.urls import path
from . import views

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('<int:id>/', views.profile, name='profile'),
  path('delete/', views.deleteAccount, name='delete-account'),
  path('update/', views.updateAccount, name='update-account')
]