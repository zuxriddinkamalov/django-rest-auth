# Django
from django.urls import path, include

# REST Framework
from rest_framework.routers import DefaultRouter

# Project
from apps.rauth.views import AuthUserView

app_name = 'apps.auth'

user_router = DefaultRouter()

urlpatterns = [
    path('', include(user_router.urls)),
    path('auth/', AuthUserView.as_view(), name='auth')
]
