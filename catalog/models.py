from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'My books'
        verbose_name_plural = 'My books'
        ordering = ['genre']