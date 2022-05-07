from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField
from articles.models import Article


def user_directory_path(instance, filename):
    return f'{instance.name}/%Y/%m/%d/'


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    #symmetrical: 서로참조
    profile_picture = ProcessedImageField(
        blank=True,
        upload_to='profile/',
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 60},
        default='../static/accounts/default_profile.jpg'
        )