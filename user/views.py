from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.parsers import JSONParser
from user.models import User
from user.serilalizers import UserSerializer


@csrf_exempt
def users(request):

    if request.method == "GET":
        users = User.objects.all()
        return render(request, 'user/user_list.html', { 'user_list': users })

    
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def login(request):

    if request.method == "GET":
        return render(request, 'user/login.html')

    if request.method == "POST":
        try:
            user_name = User.objects.get(user_name=request.POST['name'])
            
            request.session['user_id'] = user_name.id
        except User.DoesNotExist:
            return render(request, 'user/login_fail.html')
        else:
            return render(request, 'user/login_success.html')