from django.urls import path
from .views import register_user, login_user, grouplist, owner_create

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('grouplist/',grouplist, name = 'grouplist'),
    path('owner_create/', owner_create, name = 'owner_create')
]


