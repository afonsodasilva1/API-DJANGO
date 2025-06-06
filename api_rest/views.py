from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_by_nick(request, nick):
    
    try: 
        user = User.objects.get(pk=nidk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if(request.method == 'GET'):

        serializer = UserSerializer(user)

        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manage(request):
    if request.method == 'GET':

        try:
            if request.GET['user']:

                user_nickname = request.GET['user']

                try:
                    user = User.objects.get(pk=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
#CRIANDO OS DADOS        
    if request.method == 'POST':

        new_user = request.data

        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

#EDITANDO OS DADOS (PUT)

    if request.method == 'PUT':

        nickmane = request.data['user_nickname']

        updated_user = User.objects.get(pk=nickmane)

        print(request.data)

        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

#DELETANDO DADOS (DELETE)

    if request.method == 'DELETE':
        try: 
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            user_to_delete.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    