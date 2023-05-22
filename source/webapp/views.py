from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article
from django.urls import reverse

def index_views(request):
    articles = Article.objects.order_by('-created_at')
    context = {
        'articles': articles
    }
    return render(request, "index.html", context)

def article_view(request, pk, *args, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)

def article_create_view(request):
    if request.method == "GET":
        return render(request, "article_create.html")
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        new_article = Article.objects.create(title=title, content=content, author=author)
        return redirect('article_view', pk=new_article.pk)

def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'article_update.html', {'article': article})
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.author = request.POST.get('author')
        article.save()
        return redirect('article_view', pk=article.pk)

def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'article_delete.html', {'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
