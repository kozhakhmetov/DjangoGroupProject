from django.db import models


class PostManager(models.Manager):

    def created_by_user(self, user):
        return super().filter(created_by=user)

    def created_by_user_detailed(self, user, pk):
        return super().filter(created_by=user, pk=pk)

    def subscribers_posts(self, user):
        subscriptions = user.user_subscriptions.all()
        allPosts = []
        for s in subscriptions:
            allPosts += s.userTo.posts
        return allPosts

    def user_saved(self, user):
        postSaved = user.user_saved.all()
        allPosts = []
        for p in postSaved:
            allPosts += p.post
        return allPosts


class CommentManager(models.Manager):
    def post_comments(self, post):
        return super().get_queryset().order_by('-created_date').filter(post=post)


class PostLikeManager(models.Manager):
    def get_post_likes(self, post):
        return post.post_likes.all()


class CommentLikeManager(models.Manager):
    def get_comment_like(self, comment):
        return comment.comment_likes.all()


class PostSavedManager(models.Manager):
    def get_user_saved(self, user):
        return super().get_queryset().filter(saved_by=user)


class SubscriptionManager(models.Manager):
    def get_user_subscriptions(self, user):
        return super().filter(userFrom=user)

class NotificationManager(models.Manager):
    def get_notifications(self, user):
        return super().filter(toUser=user)
