from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    about = AboutCategory.objects.all()
    description = Description.objects.all()

    data = {
        'about': about,
        'description': description,
    }
    return render(request, 'main/index.html', data)
