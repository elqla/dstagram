from django.contrib import admin
from .models import Article, Comment, Bookmark, Picture

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Picture)
admin.site.register(Bookmark)