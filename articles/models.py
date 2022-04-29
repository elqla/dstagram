from django.conf import settings
from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

#USER
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 유저1: 게시글 N   -- 유저 1에 게시글 무엇인지 알림
    # table에 user_id 자동으로 생성됨 ### table 확인해보기 __user 가 article을 어떻게 역참조 하는지 
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Bookmark', related_name='book_articles', blank=True) # 북마크 테이블 가져오기

    def __str__(self):
        return f'{self.user},{self.content},{self.like_users},{self.created_at},{self.book_users}'


class Picture(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    upload_picture = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(500, 500)],
        format='JPEG',
        options={'quality': 60})
    #image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return f'{self.upload_picture}'

    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments') #내가 좋아요누른댓글들
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# bookmark = models.ManyToMany
class Bookmark(models.Model): ## 북마크에서 역참조를 할수 없음
    title = models.CharField(max_length=20) #### title을 쓰기 위해 bookmark를 새로 만들어줌
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #user.bookmark_set == usr가 bookmark한 pk가 나온다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    #북마크 #아티클