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



## 220422

### Hiding elements

| **Screen Size**                           | **Class**                      |
| ----------------------------------------- | ------------------------------ |
| Hidden on all (모든 화면에서 숨기기)      | .d-none                        |
| Hidden only on xs (xs 크기에서만 숨기기)  | .d-none .d-sm-block            |
| Hidden only on sm (sm 크기에서만 숨기기)  | .d-sm-none .d-md-block         |
| Hidden only on md (md 크기에서만 숨기기)  | .d-md-none .d-lg-block         |
| Hidden only on lg (lg 크기에서만 숨기기)  | .d-lg-none .d-xl-block         |
| Hidden only on xl (xl 크기에서만 숨기기)) | .d-xl-none                     |
| Visible on all (모든 화면에서 보이기)     | .d-block                       |
| Visible only on xs (xs 크기에서만 보이기) | .d-block .d-sm-none            |
| Visible only on sm (sm 크기에서만 보이기) | .d-none .d-sm-block .d-md-none |
| Visible only on md (md 크기에서만 보이기) | .d-none .d-md-block .d-lg-none |
| Visible only on lg (lg 크기에서만 보이기) | .d-none .d-lg-block .d-xl-none |
| Visible only on xl (xl 크기에서만 보이기) | .d-none .d-xl-block            |

[참고](https://velog.io/@leyuri/bootstrap4-브라우저-크기-별-요소-hidden-visible)

navbar 만듦

```django
#base.html
<script src="https://kit.fontawesome.com/4369db3be1.js" crossorigin="anonymous"></script> // icon쓰기
{% load static %}
<link rel="stylesheet" href="{% static "style.css" %}">

#_navbar include해서 써보기
{% load static %}
static/style.css
```

prittier

```
prettier.printWidth (default: 200)
"esbenp.prettier-vscode"
```

index page 틀 만들기

- 아직 다 못함
- [참고해서 마저하기](https://ojji.wayful.com/2013/12/HTML-set-Two-Parallel-DIVs-columns.html)









##