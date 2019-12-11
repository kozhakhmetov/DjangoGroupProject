from django.urls import path
from rest_framework.routers import DefaultRouter
from core.views.viewSets import *
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

urlpatterns = [
    path('api/token/', obtain_jwt_token, name='token_obtain'),
    path('api/refresh/', refresh_jwt_token, name='token_refresh'),
    path('posts/', PostViewSet),
]