from django.shortcuts import get_object_or_404, redirect, render

from articles.models import Article, Picture
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_safe, require_http_methods, require_POST
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
def detail(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm()
        comments = article.comment_set.all()
        context = {
            'article':article,
            'comment_form':comment_form,
            'comments':comments,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')

@require_http_methods(['GET', 'POST'])
def comment_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk = pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


