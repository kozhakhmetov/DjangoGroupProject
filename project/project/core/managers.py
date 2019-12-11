from django.db import models


class PostManager(models.Manager):

    def created_by_user(self, user):
        return user.posts.all().order_by('-created_date')

    def subscribers_posts(self, user):
        subscriptions = user.user_subscriptions.all()
        allPosts = []
        for s in subscriptions:
            allPosts += s.post
        return allPosts

    def user_saved(self, user):
        postSaved = user.user_saved.all()
        allPosts = []
        for p in postSaved:
            allPosts += p.post
        return allPosts


class CommentManager(models.Manager):
    def post_comments(self, post):
        return super(PostManager, self).get_queryset().order_by('-created_date').filter(post=post)


class PostLikeManager(models.Manager):
    def get_post_likes(self, post):
        return post.post_likes.all()


class CommentLikeManager(models.Manager):
    def get_comment_like(self, comment):
        return comment.comment_likes.all()


class PostSavedManager(models.Manager):
    def get_user_saved(self, user):
        return user.user_saved.all();


class SubscriptionManager(models.Manager):
    def get_user_subscriptions(self, user):
        return user.user_subscriptions.all();
