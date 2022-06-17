from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def compare(request):
    return render(request, 'compare.html')

def search(request):
    search_item = request.GET['search_item']
    return render(request, 'compare.html', {'search':search_item})
