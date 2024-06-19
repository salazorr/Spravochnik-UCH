from django.shortcuts import render
from .models import Category, University


def home(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, 'index.html', context)

def infzav(request, university_name):
    university = University.objects.get(name=university_name)

    context = {
        "university": university
    }

    return render(request, 'infzav.html', context)

def list(request, category_name=None):
    query = request.GET.get('q')
    
    if query:
        universities = University.objects.filter(shortName__iregex=query)
        category_name = 'Поиск'
    elif category_name:
        universities = University.objects.filter(type__name=category_name)
    else:
        universities = University.objects.all()

    context = {
        "category_name": category_name,
        "universities": universities,
        "query": query,
    }

    return render(request, 'list.html', context)

def search(request):
    query = request.GET.get('q')
    if query:
        results = University.objects.filter(shortName__iregex=query)
    else:
        results = University.objects.none()
    
    context = {
        'universities': results,
        'category_name': 'Поиск',
        'query': query,
    }
    return render(request, 'list.html', context)