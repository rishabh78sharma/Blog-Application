from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from main import models

# Create your views here.
def index(request):
    latest_article = models.Article.objects.all().order_by('-createdAt')[:10]
    data = {
        'latest_article': latest_article
    }
    return render(request, 'main/index.html', data)



def article(request, pk):
    try:
        article = get_object_or_404(models.Article, pk=pk)

    except:
         raise Http404() 

    data = {

        'article' : article
    }

    return render(request, 'main/article.html', data) 


def author(request, pk):

    try:
        
        author = get_object_or_404(models.Author, pk=pk)

    except:

        raise Http404()

    data = {

        'author': author
    }    


    return render(request, 'main/author.html', data) 


def create_article(request):

    authors = models.Author.objects.all()

    data = {
        'authors': authors
    }

    if request.method == "POST":
        article_data = {
            'title': request.POST['title'],
            'content': request.POST['content']
        }
        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.filter(pk = request.POST['author'])
        article.authors.set(author)

        data['sucess'] = True



    return render(request, 'main/create.html', data)


