from django.shortcuts import get_object_or_404, redirect, render

from articles.models import Article, Picture
from .forms import ArticleForm
from django.views.decorators.http import require_safe, require_http_methods
from django.contrib.auth.decorators import login_required


@require_safe
def index(request):
    if request.user.is_authenticated:
        articles = Article.objects.order_by('-pk')
        context = {
            'articles':articles,
        }
        return render(request, 'articles/index.html', context) 
    return redirect('accounts:login')

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article = form.save()
            picture = Picture()
            picture.article = article
            picture.upload_picture = form.cleaned_data.get('picture')
            picture.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, user, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk = article_pk)

        context = {
            'article':article,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')

