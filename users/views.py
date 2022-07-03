from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer

@api_view(["GET", "POST", "PUT", "DELETE"])
@parser_classes([JSONParser])
def users(request):
    print("1.users로 들어옴")
    try:
        if request.method == 'GET':
            print("2. GET 들어옴")
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            print("2. POST 들어옴")
            serializer = UserSerializer(data=request.data)
            print('serializer', serializer)
            if serializer.is_valid():
                serializer.save()
                print('3. 들어온 내부값:', serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.method == 'PUT':
            return JsonResponse({'users': 'fail'})
        elif request.method == 'DELETE':
            return JsonResponse({'users': 'fail'})
    except:
        return JsonResponse({'users': 'fail'})
