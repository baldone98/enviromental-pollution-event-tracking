from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.index, name="index"),
    path("report/", views.report_view, name="report"),
]
