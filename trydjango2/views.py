'''
   render html pages
'''

from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string, get_template



def home_view(request):
    '''
    take in a request 
    and return a html response
    '''

    article_object = Article.objects.get(id = 3)

    name = 'Margaret Mwaura'
    number = random.randint(10, 398929)

   # This is a new version of string interpolation
   #  HTML_STRING = f''' <h1> Hello {article_object.title}  - {article_object.content} </h1> '''

   # This is an old version of string interpolation that is using a dictionary

   #  Just bear in mind this is not a list it is a query set becasue we can do more things
    my_list_query_set = Article.objects.all()

   #  [102, 103, 104, 105, 1902, 289]
   #  my_list_str = ""

   #  for x in my_list:
   #     my_list_str += f"number is {x} \n"
      #  "number is " + str(x) + "\n"

    context = {
      'my_list' : my_list_query_set,
      'title' : article_object.title,
      'content' : article_object.content,
      'id' : article_object.id,
   }

   # This is the uncommon way of rendering templates
   #  tmpl = get_template("home-view.html")
   #  tmpl.string = tmpl.render(context = context)

    HTML_STRING = render_to_string("home-view.html", context = context)

   #  This string interpolation allows for the use of a dictionary
   #  HTML_STRING = ''' <h1> Hello {title}  - {content} </h1> '''.format(**context)

    print(1000*244)
    return HttpResponse(HTML_STRING)