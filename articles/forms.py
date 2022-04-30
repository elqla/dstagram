from django import forms
from .models import Article, Picture, Comment


class ArticleForm(forms.ModelForm):
    picture = forms.ImageField()
    class Meta:
        model = Article
        fields = ('content', 'picture',)


# class PictureForm(forms.ModelForm):

class CommentForm(forms.ModelForm):
    content = forms.CharField()
    class Meta:
        model = Comment
        fields = ('content',)


    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # content = models.TextField()
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments') #내가 좋아요누른댓글들
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

