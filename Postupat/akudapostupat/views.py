from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, University


def home(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, 'index.html', context)

def infzav(request, university_name):

    university = University.objects.get(name=university_name)

    context ={
        "university": university
    }

    return render(request, 'infzav.html', context)

def list(request, category_name):
    universities = University.objects.all()

    print(category_name)

    context = {
        "category_name": category_name,
        "universities": universities
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
        'category_name': 'Поиск'
    }
    return render(request, 'list.html', context)
