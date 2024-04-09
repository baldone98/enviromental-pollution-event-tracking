from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.index, name="index"),
    path("search/", views.search_view, name="search"),
    path("report/", views.report_view, name="report"),
    path("wordcloud/", views.wordcloud_view, name="wordcloud"),
    path("maptracking/", views.maptracking_view, name="maptracking"),
    path("register/", views.register, name='register'),
    path("login/", views.user_login, name='login'),

]