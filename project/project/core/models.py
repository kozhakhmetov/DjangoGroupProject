from django.db import models
from users.models import MainUser
from core.managers import (PostManager,
                           CommentManager,
                           PostLikeManager,
                           SubscriptionManager,
                           CommentLikeManager,
                           PostSavedManager,
                           NotificationManager)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='posts')
    views = models.BigIntegerField(default=0)
    category = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    header = models.CharField(max_length=1000, blank=True)
    posts = PostManager()
    liked_by = models.ManyToManyField(MainUser, related_name='liked_posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.created_by}: {self.views}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    reply_to = models.IntegerField(null=True, default=0)
    created_by = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, default='')
    comments = CommentManager()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.created_by}: {self.post}'


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    likes = PostLikeManager()

    class Meta:
        verbose_name = 'PostLike'
        verbose_name_plural = 'PostLikes'

    def __str__(self):
        return f'{self.created_by}: {self.post}'


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    likes = CommentLikeManager()

    class Meta:
        verbose_name = 'CommentLike'
        verbose_name_plural = 'CommentLikes'

    def __str__(self):
        return f'{self.created_by}: {self.comment}'


class PostSaved(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    saved_by = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='saved_by')
    post_saved = PostSavedManager()

    class Meta:
        unique_together = (('saved_by', 'post'),)
        verbose_name = 'PostSaved'
        verbose_name_plural = 'PostSaved'

    def __str__(self):
        return f'{self.post}: {self.saved_by}'


class Subscription(models.Model):
    userFrom = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='user_subscriptions')
    userTo = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    subscriptions = SubscriptionManager()

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return f'{self.userFrom} -> {self.userTo}'

# class Statistics(models.Model):
#     prev_date = models.DateField(null=True)
#     current = models.DateField(null=True)
#     owner = models.ForeignKey(MainUser, on_delete=models.CASCADE)


class Notification(models.Model):
    toUser = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='users_notifications')
    msg = models.TextField(null=True, max_length=100)
    notifications = NotificationManager()

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f'Dear {self.toUSer.username} you have new message : {self.msg}'