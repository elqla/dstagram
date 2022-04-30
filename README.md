## 220419

- Instagram model 생성

<img src="images/instagram_clone.PNG" alt="instagram_clone" style="zoom:150%;" />.



## 220420

install

```python
git ignore
django==3.2.12
pip freeze > requirements.txt
```

```python
django-admin startproject dstagram .
django-admin startapp articles
django-admin startapp accounts
pip install django-imagekit
pip install pillow
```

user_setting

```python
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
  MEDIA_ROOT = BASE_DIR/ 'media'   # 유저 업로드시 자동 폴더생성(실제 db엔 파일 경로 저장됨)
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
          upload_to='thumbnails/',   # 'thumbnails/%Y/%m/%d/'
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

prettier

```
prettier.printWidth (default: 200)
"Glavin001.unibeautify-vscode"
"esbenp.prettier-vscode"  --- 장고 이상해져서 다시 바꿈
```

index page 틀 만들기

- 아직 다 못함

- [참고해서 마저하기](https://ojji.wayful.com/2013/12/HTML-set-Two-Parallel-DIVs-columns.html)

  

## 0424

index page의 큰 틀을 잡음

- 좌측은 스크롤이 되지만, 우측은 고정되어있어야 한다.   __~~동기의 도움받음~~_
- lg-start로 lg 이상일땐 좌측정렬해서 `차례대로` div가 존재하도록  ! 

```html
<div class="container d-flex flex-row justify-content-center justify-content-lg-start" style="max-width:975px;">
   <div class="row">
      <div class="" style="height:1000px; width:650px;">
        {% for article in articles %}
        {% endfor %}
    </div>
  </div>
  <div class="d-none d-lg-block position-fixed bg-primary" style="height:200px; width:325px; left:50%; transform: translate(163px, 0);">
    <p>오른쪽</p>
  </div>
</div>
```







## 0429

- index.html 게시글 업로드 확인완료
- detial.html 게시글 card > div div 로 나누기 완료 (+반응형)
- 다음에 할 것 - > detail.html 만들기 + comment기능 + 기본 user프로필 만들기



## 0430

- login_form 삽입 



- comment기능 간단히 구현하기

- index.html 완벽

- sign_up ? 가입..?

  

- 프로필 편집====user update - 자기 프로필 사진 넣어서 user 수정 할 수 있게
