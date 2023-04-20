from django.urls import path

from users import views

urlpatterns = [
    path('', views.CreateUserAPIView.as_view(), name='user'),
    path('me/', views.MyUserAPIView.as_view(), name='me'),
]
