from django.db import models
from django.contrib.postgres.fields import JSONField  # If using PostgreSQL

class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    location = models.CharField(max_length=100, default="Tennessee Pollution") 
    terms = models.CharField(max_length=255, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    cities = models.CharField(max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=True) 

    def __str__(self):
        return f"{self.title} ({self.location})"
    
    
class SearchQuery(models.Model):
    query = models.CharField(max_length=255)
    results = models.JSONField(null=True)
    searched_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    articles = models.ManyToManyField(Article, related_name='search_queries')

    def __str__(self):
        return self.query
