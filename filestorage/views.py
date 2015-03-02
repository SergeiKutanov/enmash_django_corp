import os
from django.shortcuts import render

# Create your views here.
from django.template.context import RequestContext
from enmashcorp.settings import STATICFILES_DIRS, BASE_DIR, MEDIA_ROOT, MEDIA_URL
from filestorage.forms import SearchForm
from filestorage.models import UploadedFile


def index(request):
    files = None
    if request.method == 'POST':
        searchForm = SearchForm(request.POST)
        if searchForm.is_valid():
            files = UploadedFile.objects.filter(
                name__icontains=searchForm.cleaned_data['searchQuery']
            )
    else:
        searchForm = SearchForm

    if files is None:
        files = UploadedFile.objects.all()

    return render(
        request,
        'filestorage/index.html',
        {
            'files': files,
            'search_form': searchForm,
            'request': request
        }
    )