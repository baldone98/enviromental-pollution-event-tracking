from django.urls import path
from . import views
from django.urls import path
from .views import fetch_articles




urlpatterns = [
    path('homepage/', views.index, name='homepage'),
    path('fetch_articles/', views.fetch_articles, name='fetch_articles'),
    path('search/', views.search, name='search'),
    path('search.html', views.search, name='search_html'),  # Add this line
    path('report/', views.report, name='report'),
    path('wordcloud/', views.wordcloud, name='wordcloud'),
    path('maptracking/', views.maptracking, name='maptracking'),
    path('index/', views.index, name='index'),
]
