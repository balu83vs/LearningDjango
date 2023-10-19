from django.shortcuts import render, redirect
from .models import Articles, Comments
from django.http import HttpResponseNotFound

# Create your views here.

def indexpage(request):
    articles = Articles.objects.all()
    return render(request, template_name='index.html', context={'articles': articles, 'page': 'index'})

def aboutpage(request):
    return render(request, template_name='about.html', context={'page': 'about'})

def contactpage(request):
    if request.method == 'GET':
        return render(request, template_name='contact.html', context={'page': 'contact'})
    else:
        with open("D:\py_learning\learning_django\learning_project\learning\lesson_2\message_result.txt", "a") as message_file:
            message_file.writelines(f'{request.POST["name"]}, {request.POST["email"]}, {request.POST["subject"]}, {request.POST["message"]}\n')
        return redirect(contactpage)
    
def postspage(request, article_id):
    article = Articles.objects.filter(id=article_id).first()
    if article:
        comments = Comments.objects.filter(Article=article).all()
        return render(request, template_name='posts.html', context={"article": article, "comments": comments})
    return HttpResponseNotFound('Article not found')

def commentpost(request, article_id):
    if request.method == 'POST':
        article = Articles.objects.filter(id=article_id).first()
        if 'name' in request.POST and 'email' in request.POST and 'message' in request.POST:
            article.new_comment(request.POST)
            return redirect(postspage, article_id)
    return HttpResponseNotFound('Ошибка 404')

