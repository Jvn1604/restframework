from turtle import position
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib import messages

from .models import staff
from .serializer import staffSerializer


@csrf_exempt
def staff_api(request, id):
    # try:
    pro = staff.objects.get(id=id)
    # except staff_api.DoesNotExist:
    #     return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = staffSerializer(pro)
        return JsonResponse(serializer.data)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = staffSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = staffSerializer(pro, data=data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request,'Data has been successfully Updated!', extra_tags="menu")
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'DELETE':
        pro.delete()
        messages.success(request,'Data has been successfully deleted!', extra_tags="menu")
        return HttpResponse(status=204)





