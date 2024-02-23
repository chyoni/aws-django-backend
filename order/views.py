from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.parsers import JSONParser
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer

@csrf_exempt
def shops(request):

    if request.method == "GET":
        shops = Shop.objects.all()
        """ serializer = ShopSerializer(shops, many=True)

        return JsonResponse(serializer.data, safe=False) """
        return render(request, 'order/shop_list.html', { 'shop_list': shops })

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return  JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def menus(request, shop_id):

    if request.method == "GET":
        menus = Menu.objects.filter(shop=shop_id)
        """ serializer = MenuSerializer(menus, many=True)
        
        return JsonResponse(serializer.data, safe=False) """
        return render(request, 'order/menus.html', { 'menus': menus, 'shop_id': shop_id })

    if request.method == "POST":
        
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return  JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def order(request):

    if request.method == "GET":

        orders = Order.objects.all()
        return render(request, 'order/order_list.html', { 'orders': orders })

    if request.method == "POST":
        address = request.POST['address']
        shop_id = request.POST['shop_id']
        food_list = request.POST.getlist('menu')
        order_date = timezone.now()
        
        order = Order.objects.create(address=address, order_date=order_date, shop_id=shop_id)
        order.save()

        for food in food_list:
            order_food = Orderfood.objects.create(order=order, food_name=food)
            order_food.save()

        return redirect('/orders')