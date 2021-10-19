from django.shortcuts import render
from .models import Article

# Create your views here.

# setting id to None means it is not required

def article_detail_view(request, id = None):
    article_object = None
    if id != None:
        article_object = Article.objects.get(id = id)
    context = {
        "object" : article_object,
    }
    return render(request, "articles/details.html", context = context)