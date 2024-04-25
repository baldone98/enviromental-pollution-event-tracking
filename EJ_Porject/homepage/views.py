from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Query
from GoogleNews import GoogleNews
from ratelimit.decorators import ratelimit


###JKK
import csv
import os
#JKK###

def index(request): 
    return render(request, "homepage/index.html")

def search_view(request):
    return render(request, "search/search.html")

def report_view(request):
    return render(request, "report/report.html")

def wordcloud_view(request):
    return render(request, "wordcloud/wordcloud.html")

def maptracking_view(request):
    return render(request, "maptracking/maptracking.html")


@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def fetch_articles(request):
    googlenews = GoogleNews()
    query = "air pollution breath Tennessee"
    articles_number = 200
    all_articles = []
    all_links = []
    page_num = 1

    while len(all_articles) <= articles_number:
        googlenews.search(query)
        articles = googlenews.get_texts()
        links = googlenews.get_links()
        all_articles.extend(articles)
        all_links.extend(links)
        googlenews.clear()
        page_num += 1
        articles_curr_page = googlenews.get_page(page_num)

    # Save articles to CSV
    with open("articles.csv", "w") as f:
        for i in range(articles_number):
            f.write('"'+all_articles[i] +'"'+ "," + all_links[i] + "\n")

    return render(request, 'articles.html', {'articles': all_articles, 'links': all_links})