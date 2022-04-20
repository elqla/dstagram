## 220419

- Instagram model 생성

<img src="images/instagram_clone.PNG" alt="instagram_clone" style="zoom:150%;" />.



## 220420

install

```
git ignore
django==3.2.12
pip freeze > requirements.txt
```

```
django-admin startproject dstagram .
django-admin startapp articles
django-admin startapp accounts
pip install django-imagekit
pip install pillow
```

user_setting

```
AUTH_USER_MODEL = 'accounts.User'
abstractuser
```

model 만들기

- 모델을 만들면서, foreginkey에 대한 이해와 manytomanyfield를 적용해보았다.

- picture를 만들면서 static경로, media경로를 나누어 주었다.

  ```python
  ## static ##
  #settings.py
  STATIC_URL = '/static/'
  
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  
  #accounts/static/accounts
  defult_profile.jpg 추가
  
  
  ## media ##
  #settings.py
  MEDIA_ROOT = BASE_DIR/ 'media'
  MEDIA_URL = '/media/'
  INSTALLED_APPS = [
      'imagekit',]
  
  #pjt/urls.py
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
      path('admin/', admin.site.urls),
  ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
  #models.py
  class Picture(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      upload_picture = ProcessedImageField(
          blank=True,
          upload_to='thumbnails/',
          processors=[Thumbnail(500, 500)],
          format='JPEG',
          options={'quality': 60})
      #image = models.ImageField(upload_to="images/", blank=True)
  ```





##