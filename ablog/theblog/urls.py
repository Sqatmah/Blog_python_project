from django.urls import path 
#from . import views
from .views import HomeView
from .views import ArticleDetailView



urlpatterns = [
    # we don't need its for the basic view 
   # path('', views.home, name='home'), 
   path('', HomeView.as_view(), name='home'),
   path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
 
]
