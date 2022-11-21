from django.shortcuts import render
from .models import News


# Create your views here.
def news(request):
    newss = News.objects.all()
    print("number of news: ", len(newss))
    return render(request, 'news.html', {'newss': newss})