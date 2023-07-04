from django.shortcuts import render
from viewer.models import APIViewer

# Create your views here.
def index(request):
    data = APIViewer()
    content = data.fetch_name_height_mass

    context = {
        'list':content
    }

    return render(request, 'index.html', context)
