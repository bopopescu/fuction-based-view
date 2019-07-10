from django.urls import path

#from .views import HomePageView, CreatePostView
from . import views


urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', views.home, name= "home"),
    #path('post/', CreatePostView.as_view(), name='add_post')
    path('post/', views.create, name='add_post'),

]