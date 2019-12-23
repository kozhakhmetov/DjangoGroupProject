from django.db.models.signals import post_save, pre_delete, post_delete, pre_save
from django.dispatch import receiver
from core.models import *
from core.models import *

#
# @receiver(pre_save, sender=Subscription)
# def notification_created_sub(sender, instance, **kwargs):
#     toUser = instance.userTo
#     text = f'{instance.userFrom.username} subscribed to you'
#     notification = Notification(toUser, text)
#     notification.save()
#
#
# @receiver(pre_save, sender=Post)
# def notification_createdPost(sender, instance, **kwargs):
#     subscribers = instance.user.user_subscriptions.all()
#     for s in subscribers:
#         toUser = instance.userTo
#         text = f'{instance.created_at.username}  added new post'
#         notification = Notification(toUser, text)
#         notification.save()
#
#

