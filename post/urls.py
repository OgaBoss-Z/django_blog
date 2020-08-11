from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home-page'),
    path('<slug>/', views.post_detail_view, name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('<pk>/<slug>/', views.category_list, name='post-category'),
]


