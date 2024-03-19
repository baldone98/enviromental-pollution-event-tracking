from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

###JKK
import csv
import os
#JKK###

def index(request): 
    return render(request, "homepage/index.html")

def report_view(request):
    return render(request, "report/report.html")

