from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def trial(request):
    # out = trial_func.delay()
    return render(request, 'trial.html')