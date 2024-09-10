from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from .models import Product, Comment
from django.core import serializers
from rest_framework.response import Response
from .serializers import ProductSerializer, CommentSerializer 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    permission_classes([IsAuthenticated])
    def post(self, request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        

class ProductRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset =Product.objects.all()
    serializer_class=ProductSerializer 
    permission_classes=[IsAuthenticated]


class CommentListAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    permission_classes([IsAuthenticated])
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class CommentDetailAPIView(APIView):
    permission_classes([IsAuthenticated])
    
    def get_object(self, pk):
        return get_object_or_404(Comment, pk=pk)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        data={"delete":f"Comment({pk}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer=CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)