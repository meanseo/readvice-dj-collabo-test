from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from users.models import User
from users.serializers import UserSerializer

@api_view(["GET", "POST", "PUT", "DELETE"])
@parser_classes([JSONParser])
def users(request):
    print("1.users로 들어옴")
    try:
        if request.method == 'GET':
            return JsonResponse({'users': 'fail'})
        elif request.method == 'POST':
            print("2. POST 들어옴")
            new_user = request.data
            print(new_user)
            serializer = UserSerializer(data=new_user)
            print('serializer', serializer)
            if serializer.is_valid():
                print("3. 들어온 내부값:"+ serializer)
                serializer.save()
                return JsonResponse({'JOIN':'SUCCESS'})
            else:
                return JsonResponse({'POST':'False'})
        elif request.method == 'PUT':
            return JsonResponse({'users': 'fail'})
        elif request.method == 'DELETE':
            return JsonResponse({'users': 'fail'})
    except:
        return JsonResponse({'users': 'fail'})
