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




def index(request):
    return render(request, "homepage/index.html")


def fetch_articles(request):
    query = request.GET.get('q', '')
    if not query:
        return render(request, "search/search.html")

    # Append 'Tennessee' to ensure locality in the search
    full_query = f"{query} Tennessee"

    googlenews = GoogleNews(lang='en')
    googlenews.search(full_query)
    results = googlenews.result()

    # Save results to database
    for result in results:
        Article.objects.get_or_create(title=result['title'], link=result['link'])

    # Fetch all articles to display
    articles = Article.objects.all()

    return render(request, 'report/report.html', {'articles': articles})

def search(request):
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    date = request.GET.get('date', '')

    # Assuming Article model has fields to match these parameters
    articles = Article.objects.filter(title__icontains=query, location__icontains=location)

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
    if search_query:
        # Retrieve the search query from the database
        query = SearchQuery.objects.filter(query=search_query).first()
        if query:
            # Assuming you have a field named 'related_articles' in your SearchQuery model
            related_articles = query.related_articles.all()
            return render(request, 'report/report.html', {'articles': related_articles})
    
    # If search query not provided or not found in the database, render an empty template
    return render(request, "report/report.html", )