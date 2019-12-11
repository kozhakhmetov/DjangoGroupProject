from django.contrib.auth.models import AbstractUser
from django.db import models
from project import settings
from utils import upload
from utils import validators


class MainUser(AbstractUser):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_login}'

    def __str__(self):
        return f'{self.id}: {self.username}'

    def send_greeting_email(self):
        pass

    def send_activate_sms(self):
        pass

    def save(self, *args, **kwargs):
        # pre save
        created = self.pk is None
        super().save(*args, **kwargs)
        # post save
        # if created:
        #     Profile.objects.create(user=self)


class Profile(models.Model):
    bio = models.TextField(max_length=500)
    avatar = models.FileField(upload_to=upload.document_path, validators=[validators.validate_file_size,
                                                                          validators.validate_extension],
                              null=True, blank=True)
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE, related_name='profiles')


    class Meta:
        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')


    def __str__(self):
        return f'{self.user}'