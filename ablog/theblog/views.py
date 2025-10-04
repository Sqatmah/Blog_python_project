from django.shortcuts import render
#this is the import for class based views
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

# Create your views here.
# this is basic view function
#def home(request):
#   return render(request, 'home.html') 

# and this is the more comment way to write a view function
#using class based views CBV 

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date'] 
   # ordering = ['-id'] # to show the latest post first we use -id


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'



class AddPostView(CreateView):
    model = Post
    form_class=PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
   # fields = ('title','body')


class UpdatePostView(UpdateView):
    model = Post
    form_class=EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home') # Redirect to home page after deletion






