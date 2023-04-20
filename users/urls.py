from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('register/',views.CustomUserRegistration.as_view(),name='register_user'),
       path('logout/blacklist/', views.BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
