import json  # Add this at the top of your file
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SearchQuery
import requests
from GoogleNews import GoogleNews
from django.shortcuts import render
import numpy as np
from PIL import Image
from io import BytesIO
from wordcloud import WordCloud
import xml.etree.ElementTree as ET
googlenews = GoogleNews()
from .models import SearchQuery, Article
from datetime import datetime




def index(request):
    return render(request, "homepage/index.html")


def fetch_articles(request):
    query_text = request.GET.get('q', '')
    if not query_text:
        return render(request, "search/search.html")

    full_query = f"{query_text} Tennessee"
    googlenews = GoogleNews(lang='en')
    googlenews.search(full_query)
    results = googlenews.result()
    search_query = SearchQuery.objects.create(
        query=query_text,
        results=json.dumps(results, default=str),  # Use a custom default to handle datetimes
        searched_on=datetime.now()
    )

    for result in results:
        article, created = Article.objects.get_or_create(
            title=result['title'],
            link=result['link'],
            defaults={
                'terms': result.get('description', ''),
                'keywords': result.get('meta_keywords', 'air,waste,water,noise'),
                'cities': 'Tennessee',  # Assume all articles pertain to Tennessee for now
                'county':result.get('location', '')  
            }
        )
        search_query.articles.add(article)

    return redirect('report')

def search(request):
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    articles = Article.objects.filter(title__icontains=query)
    if location:
        articles = articles.filter(location__icontains=location)

    return render(request, 'search/search.html', {'articles': articles})



def generate_word_cloud(request):
    text = ' '.join(query.query for query in SearchQuery.objects.all())
    wordcloud = WordCloud(width=800, height=400).generate(text)
    response = HttpResponse(content_type="image/png")
    image = wordcloud.to_image()
    image.save(response, "PNG")
    return response

def maptracking(request):
    return render(request, "maptracking/maptracking.html")



def report(request):
    search_query = request.GET.get('q', None)
    articles = Article.objects.none()  # Start with no articles
    if search_query:
        query = SearchQuery.objects.filter(query=search_query).first()
        if query:
            articles = query.articles.all()
    else:
        articles = Article.objects.all().order_by('-id')

    return render(request, 'report/report.html', {'articles': articles})