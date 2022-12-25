from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Movie(models.Model): 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)

class Review(models.Model):
    text = models.CharField(max_length=250) # stores the review text
    date = models.DateTimeField(auto_now_add=True) # stores the date the review was created
    user = models.ForeignKey(User, on_delete=models.CASCADE) # stores the user who created the review. Allos many-to-one relationship
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # stores the movie the review is for
    watchAgain = models.BooleanField(default=False) # stores whether the user would watch the movie again

    def __str__(self):
        return self.text

