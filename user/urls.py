from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserCreateView, UserLoginView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('login', UserLoginView.as_view()),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
