from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer

@csrf_exempt
def shops(request):

    if request.method == "GET":
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return  JsonResponse(serializer.errors, status=400)
    
