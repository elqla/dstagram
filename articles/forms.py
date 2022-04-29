from django import forms
from .models import Article, Picture


class ArticleForm(forms.ModelForm):
    picture = forms.ImageField()
    class Meta:
        model = Article
        fields = ('content', 'picture',)


# article = models.ForeignKey(Article, on_delete=models.CASCADE)
# upload_picture 