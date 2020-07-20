from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import ProjectDetailView

urlpatterns = [
    path('', views.home, name='home-page'),
    path('<slug>/', views.post_detail_view, name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.about, name='blog-contact'),
]


