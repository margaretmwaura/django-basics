from django.shortcuts import render
from .models import Article

# Create your views here.

# setting id to None means it is not required 

def article_search_view(request):
    print(request.GET)

    query_dict = request.GET # thid is a dictionary

    try:
        query = int(query_dict.get("query"))
    except:
        query = None

    article_object = None

    if query is not None:
        article_object = Article.objects.get(id = query)

    context = {
        'object' : article_object,
    }
   
    print(article_object)

    return render(request, "articles/search.html", context=context)


def article_create_view(request):

    if request.method == "POST":
        
        query_dict = request.POST
        title = query_dict.get("title")
        content = query_dict.get("content")

        if title is not None and content is not None:

            # This is another way of saving to the database

            # article = Article()
            # article.title = title
            # article.content = content
            # article.save() 

            Article.objects.create(title = title , content = content)

    context = {
    }
    return render(request, "articles/create.html", context = context)


def article_detail_view(request, id = None):
    article_object = None
    if id != None:
        article_object = Article.objects.get(id = id)
    context = {
        "object" : article_object,
    }
    return render(request, "articles/details.html", context = context)