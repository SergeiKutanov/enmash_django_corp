from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# @login_required(login_url='/login/')
from news.models import NewsItem


def index(request):

    news = NewsItem.objects.filter(publish=True).order_by('-created_at')[0:5]

    return render(
        request,
        'enmashcorp/index.html',
        {
            'news': news
        }
    )


def login_action(request):

    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            login(request, user)
            return HttpResponseRedirect(
                reverse('index')
            )

    return render(
        request,
        'enmashcorp/login.html'
    )


def logout_action(request):
    logout(request)
    return HttpResponseRedirect(
        reverse('index')
    )