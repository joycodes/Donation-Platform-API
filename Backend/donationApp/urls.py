from django.urls import path, include
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('About/', views.About, name='About'),
        path('blog/', views.blog, name='blog'),
        path('single-blog/', views.single_blog, name='single-blog'),
        path('contact/', views.contact, name='contact'),
        path('Cause/', views.cause, name='Cause'),
        path('cause_details/', views.cause_details, name='cause_details'),
        path('elements/', views.elements, name='elements'),
        path('donate/', views.donate, name='donate'),


]