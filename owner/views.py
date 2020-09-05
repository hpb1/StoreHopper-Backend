from django.shortcuts import render
from .models import Store
from .serializers import StoreSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
# Create your views here.

class StoreRegister(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self,request)
    owner = request.user.id
    obj = Store.objects.get(owner=owner)
    serializer = StoreSerializer(obj, many=True)
    return Response(serializer.data,status=200)


    def post(self,request):
        request.data['owner'] = request.user.id
        obj = StoreSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({
                'status': 'added'
            },status=201)
        else:
            return Response({
                'Invalid request.'
            }, status=400)

    def patch(self,request,pk):
        obj = Store.objects.get(id=pk)
        serializer = StoreSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response({
                'Store does not exist.'
            })


    def delete(self,request,pk):
        try:
            obj = Store.objects.filter(id=pk)
            obj.delete()
            return Response({
                'status': 'deleted'
            },status=200)
        except:
            return Response({
                'Store not found.'
            },status=404)

class StoreProximity(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self,request):
        try:
            zip_code = request.data['zip_code']
            obj = Store.objects.filter(zip_code=zip_code)
            serializer = StoreSerializer(obj, many=True)
            return Response(serializer.data, status=200)
        except:
            return Response({
                'No stores found.'
            }, status=400)

class StoreCityProximity(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self,request):
        try:
            city = request.data['city']
            obj = Store.objects.filter(city=city)
            serializer = StoreSerializer(obj, many=True)
            return Response(serializer.data, status=200)
        except:
            return Response({
                'No stores found.'
            }, status=400)
