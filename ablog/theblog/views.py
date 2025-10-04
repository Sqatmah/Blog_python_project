from django.shortcuts import render
#this is the import for class based views
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# this is basic view function
#def home(request):
#   return render(request, 'home.html') 

# and this is the more comment way to write a view function
#using class based views CBV 

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'






