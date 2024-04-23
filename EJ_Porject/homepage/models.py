from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=255)
    date_fetched = models.DateTimeField(auto_now_add=True)

    
