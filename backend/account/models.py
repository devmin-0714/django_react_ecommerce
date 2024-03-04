from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    username = models.CharField(max_length=50, unique=True, verbose_name='사용자 ID')
    email = models.EmailField(unique=True, verbose_name='이메일')


def user_directory_path(instance, filename):
    user = getattr(instance, 'user', None)

    user_id = user.id if user else 'file'
    extension = filename.split('.')[-1]
    new_filename = f'{user_id}.{extension}'

    return f'user_{user_id}/{new_filename}'
