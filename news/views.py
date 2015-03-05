from django.shortcuts import render
from news.models import NewsItem


def index(request):

    news = NewsItem.objects.filter(publish = True).order_by('-created_at')

    return render(
        request,
        'news/index.html',
        {
            'news': news
        }
    )