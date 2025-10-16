from django.urls import path 
#from . import views
from .views import HomeView
from .views import ArticleDetailView, AddPostView, UpdatePostView,DeletePostView



urlpatterns = [
    # we don't need its for the basic view 
   # path('', views.home, name='home'), 
   path('', HomeView.as_view(), name='home'),
   path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
   path('add_post/', AddPostView.as_view(), name='add_post'),
   path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
   path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
   
   

]
