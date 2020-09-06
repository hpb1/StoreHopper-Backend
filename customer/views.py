from django.shortcuts import render
from .models import ItemRequest
from .serializers import RequestSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
# Create your views here.

class CustomerRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self,request): #store id
        try:
            obj = ItemRequest.objects.filter(customer=request.user.id)
            serializer = RequestSerializer(obj, many=True)
            return Response(serializer.data,status=200)
        except:
            return Response({
                'Invalid Request.'
            }, status=400)

    def post(self,request,pk): #store id
        request.data['customer'] = request.user.id
        request.data['store'] = pk
        obj = RequestSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response({
                'status': 'added'
            },status=201)
        else:
            return Response({
                'Invalid request.'
            }, status=400)

    def delete(self,request,pk): #itemrequest id
        try:
            obj = ItemRequest.objects.get(id=pk)
            obj.delete()
            return Response({
                'status': 'deleted'
            },status=200)
        except:
            return Response({
                'Store not found.'
            },status=404)

class StoreRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get(self,request,pk): #store id
        try:
            obj = ItemRequest.objects.filter(store=pk, fulfillment=False)
            serializer = RequestSerializer(obj, many=True)
            return Response(serializer.data,status=200)
        except:
            return Response({
                'Requests not found.'
            },status=404)

    def post(self, request, pk): #itemrequest id
        try:
            obj = ItemRequest.objects.get(id=pk)
            obj.fulfillment = True
            obj.save()
            return Response({
                'status': 'fulfilled'
            },status=200)
        except:
            return Response({
                'Request not found.'
            },status=404)
