from django.shortcuts import render
#this is the import for class based views
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
from theblog.repositories.post_repository import PostRepository

# Create your views here.
# this is basic view function
#def home(request):
#   return render(request, 'home.html') 

# and this is the more comment way to write a view function
#using class based views CBV 



repo = PostRepository()



class HomeView(ListView):
    #model = Post
    template_name = 'home.html'
    #ordering = ['-post_date'] 
   # ordering = ['-id'] # to show the latest post first we use -id

    def get_queryset(self): ## using repo pattern to bring all posts
        return repo.get_all_posts()




class ArticleDetailView(DetailView):
    #model = Post
    template_name = 'article_details.html'

    def get_object(self,queryset=None):  ## using repo pattern to bring a single post by id
        #post_id = self.kwargs.get('pk')
        return repo.get_post_by_id(self.kwargs.get('pk'))




class AddPostView(CreateView):
    #model = Post
    form_class=PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
   # fields = ('title','body')
    def form_valid(self, form):
        repo.create_post(
            title=form.cleaned_data['title'],
            title_tag=form.cleaned_data['title_tag'],
            author=form.cleaned_data['author'],
            body=form.cleaned_data['body']
        )
        return super().form_valid(form)
    






class UpdatePostView(UpdateView):
    #model = Post
    form_class=EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']

    def get_object(self,queryset=None):  ## using repo pattern to bring a single post by id
        return repo.get_post_by_id(self.kwargs.get('pk'))
    




class DeletePostView(DeleteView):
    #model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home') # Redirect to home page after deletion

    def get_object(self,queryset=None):  ## using repo pattern to bring a single post by id
        return repo.get_post_by_id(self.kwargs.get('pk'))






