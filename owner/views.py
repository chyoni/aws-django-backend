from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from order.models import Order

@csrf_exempt
def make_order_estimated_time(request, order_id):

    if request.method == "GET":

        pass

    if request.method == "POST":
        
        order = Order.objects.get(pk=order_id)
        
        estimated_time = request.POST['estimated_time']

        order.estimated_time = estimated_time
        
        order.save()

        return redirect('/orders')