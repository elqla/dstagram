from django.conf import settings
from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    # user: Articles  1:N 이니까, article_set이 foriegnkey를 가짐
    # user가 article을 역참조
    # user는 무슨 글을 썼는지 모르므로, 역참조를 함

    # Article.user가 내가 참조한 유저
    # user.article_set 나를 참조한 아티클들
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # foreignkey_integerfield
    #article: like_users이지만, M:N은 like_user와 article이 서로 foriegnkey를 가질 수 있다.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Picture(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    upload_picture = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(500, 500)],
        format='JPEG',
        options={'quality': 60})
    #image = models.ImageField(upload_to="images/", blank=True)


    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments') #내가 좋아요누른댓글들
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bookmark(models.Model):
    user = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    article = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
