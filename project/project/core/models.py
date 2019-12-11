from django.db import models
from users.models import MainUser

# class PostManager(models.Manager): # get posts with likes and comments
#     pass
#
#
# class FullPost(models.Model): # get request for Post
#     pass

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='posts')
    views = models.BigIntegerField(default=0)
    category = models.IntegerField(default=0)
    description = models.TextField(null=True)
    # posts = PostManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.created_by}: {self.views}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    reply_to = models.IntegerField(null=True)
    created_by = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.created_by}: {self.post}'

class Post_like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    created_by = models.IntegerField(null=False)
    class Meta:
        verbose_name = 'Post_Like'
        verbose_name_plural = 'Post_likes'

    def __str__(self):
        return f'{self.created_by}: {self.post}'

class Comment_like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')
    created_by = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Comment_like'
        verbose_name_plural = 'Comment_likes'

    def __str__(self):
        return f'{self.created_by}: {self.comment}'

class Post_saved(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_saved')
    created_by = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Post_saved'
        verbose_name_plural = 'Post_saved'

    def __str__(self):
        return f'{self.created_by}: {self.post}'

class Subscription(models.Model):
    userFrom = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='user_subscriptions')
    userToId = models.IntegerField(null=False)
    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return f'{self.userFrom} -> {self.userTo}'
# class Statistics(models.Model):
#     prev_date = models.DateField(null=True)
#     current = models.DateField(null=True)
#     owner = models.ForeignKey(MainUser, on_delete=models.CASCADE)



