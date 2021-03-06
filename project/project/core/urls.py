from django.urls import path
from rest_framework.routers import DefaultRouter
from core.views.PostViews import PostListViewSet, OwnPostViewSet, SavedPostCreateListDelete
from core.views.SubscriptionViews import SubscriptionViewSet, SubscriptionListViewSet
from core.views.CommentViews import CommentListViewSet, CommentViewSet

from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

urlpatterns = [
    path('token/', obtain_jwt_token, name='token_obtain'),
    path('refresh/', refresh_jwt_token, name='token_refresh'),
    path('posts/saved/', SavedPostCreateListDelete.as_view(), name='saved_posts'),
    path('comments/<int:pk>/', CommentListViewSet.as_view({'get': 'comment_to_post'})),
    path('subscriptions/<int:pk>/', SubscriptionListViewSet.as_view({'get' : 'subscription_of_user'}))
]

router = DefaultRouter()
router.register('posts', PostListViewSet, base_name='posts')
router.register('my_posts', OwnPostViewSet, base_name='my_posts')
# router.register('comments', CommentListCreateViewSet, base_name='comments')
router.register('comment', CommentViewSet, base_name='comments')
router.register('subscription', SubscriptionViewSet, base_name='subscriptions')
urlpatterns += router.urls
