from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        app_label="app3"
        
        

