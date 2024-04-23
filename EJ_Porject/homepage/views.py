from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Query
from GoogleNews import GoogleNews

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


def fetch_articles(request):
    googlenews = GoogleNews()
    query_text = "air pollution breath Tennessee"
    articles_number = 200
    all_articles = []
    all_links = []
    page_num = 1

    # Save the query to the database
    query_obj = Query.objects.create(query_text=query_text)

    while len(all_articles) <= articles_number:
        googlenews.search(query_text)
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
            f.write(f'"{all_articles[i]}",{all_links[i]}\n')

    return render(request, 'article/articles.html', {'articles': all_articles, 'links': all_links})
