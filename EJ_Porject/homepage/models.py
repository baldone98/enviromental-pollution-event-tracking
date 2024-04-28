from django.db import models
from django.contrib.postgres.fields import JSONField  # If using PostgreSQL

class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    location = models.CharField(max_length=100, default="Tennessee Pollution")  # Default as Tennessee

    def __str__(self):
        return f"{self.title} ({self.location})"
    
    
class SearchQuery(models.Model):
    query = models.CharField(max_length=255)
    results = models.JSONField()
    searched_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
