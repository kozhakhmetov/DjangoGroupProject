from django.urls import path
from rest_framework.routers import DefaultRouter
from core.views import PostViews
from core.views.viewSets import *
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

urlpatterns = [
    path('token/', obtain_jwt_token, name='token_obtain'),
    path('refresh/', refresh_jwt_token, name='token_refresh'),
    # path('my_posts/', PostViews.OwnPostViewSet.as_view({'get': 'list'}), name='my_pos#s')
]

router = DefaultRouter()
router.register('posts', PostViews.PostListViewSet, base_name='posts')
router.register('my_posts', PostViews.OwnPostViewSet, base_name='my_posts')


urlpatterns += router.urls
