from django.urls import path
from . import views
from django.urls import path
from .views import fetch_articles
from django.urls import path
from .views import generate_word_cloud




urlpatterns = [
    path('homepage/', views.index, name='homepage'),
    path('fetch_articles/', views.fetch_articles, name='fetch_articles'),
    path('search/', views.search, name='search'),
    path('search.html', views.search, name='search_html'),  # Add this line
    path('report/', views.report, name='report'),
    path('word-cloud/', generate_word_cloud, name='word_cloud'),
    path('maptracking/', views.maptracking, name='maptracking'),
    path('index/', views.index, name='index'),
]
