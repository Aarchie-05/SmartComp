import json
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from compare.flipkart_deals import *
from .tasks import *
from django.views.generic import View
# Create your views here.

def compare(request):
    return render(request, 'compare.html')

def search(request):
    search_item = request.GET['search_item']
    return render(request, 'compare.html')

class AjaxHandlerView(View):
    def get(self, request):
        search = request.GET.get('search')
        store = request.GET.get('store')
        req_data = request.GET.get('req_data')
        data = {}
        if req_data == 'primary':
            if store == 'flipkart':
                data = flipkart_primary_deal.delay(search)
            elif store == 'amazon':
                data = amazon_primary_deals.delay(search)
            elif store == 'snapdeal':
                data = snapdeal_primary_deal.delay(search)
        elif req_data == 'other':
            if store == 'flipkart':
                data = flipkart_other_deals.delay(search)
            elif store == 'amazon':
                data = amazon_other_deals.delay(search)
            elif store == 'snapdeal':
                data = snapdeal_other_deals.delay(search)
        
        return JsonResponse(data.get(), status=200, safe=False)
            
        # return JsonResponse([{'found':'false', 'out':str(out.get())}], status=200, safe=False)


