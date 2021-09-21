from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
import os
#def index(request):
    
#    name = request.GET.get('name') or 'world'
#    return HttpResponse(f"Hello {name} from Django!!!!")

def index(request):
    name = 'Jochimin'
    return render(request, 'base.html', {'name': name})

def search(request):
    search = request.GET.get('search')
    return render(request, 'search.html', {'search': search})