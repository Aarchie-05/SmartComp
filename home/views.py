from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .tasks import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

class AjaxHandlerView(View):
    def get(self, request):
        store = request.GET.get('store')
        req_data = request.GET.get('req_data')

        if req_data == 'best-deals':
            if store == 'flipkart':
                pass
            elif store == 'amazon':
                data = amazon_best_deals.delay()
            elif store == 'snapdeal':
                data = snapdeal_best_deals.delay()

        return JsonResponse({'data': data.get()}, status=200)
          
