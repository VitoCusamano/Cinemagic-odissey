from django.db import models


class Article(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    slug=models.SlugField() 
    thumb=models.ImageField(default="default.png",blank=True)
    
    #author=

    def __str__(self):  
        return self.title
    
    def snippet(self):
        return self.body[:50]+"..."
    
class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField()
