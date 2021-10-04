from django.shortcuts import render
from base.models import About


# Create your views here.


def index(request):
    about = About.objects.all()

    data = {
        'about': about,
    }
    return render(request, 'main/index.html', data)
