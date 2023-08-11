from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('register/', views.register_request, name='register'),
    path('search/', views.search_view, name='search'),
    path('register/login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
   # path('downloader/', views.downloader, name='downloader'),
    
    path('social_integration/', views.social_integration, name='social_integration'),


    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    
]
