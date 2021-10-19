from django.db import models

# Create your models here.

# Passing the models.Model means inherit from models.Model
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

