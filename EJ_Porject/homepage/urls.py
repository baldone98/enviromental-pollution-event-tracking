from django.urls import path
from . import views
from django.urls import path
from .views import fetch_articles

urlpatterns = [
    path("homepage/", views.index, name="index"),
    path("search/", views.search_view, name="search"),
    path("report/", views.report_view, name="report"),
    path("wordcloud/", views.wordcloud_view, name="wordcloud"),
    path("maptracking/", views.maptracking_view, name="maptracking"),
    path('fetch-articles/', views.fetch_articles, name='fetch_articles'),

]
