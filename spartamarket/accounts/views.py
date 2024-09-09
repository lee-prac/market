from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes #해당 뷰에 대한 권한 검사를 수행. 인증된 사용자만 접근.
from .models import User
from django.core import serializers
from rest_framework.response import Response
from .serializers import UserSignupSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# Create your views here.

@api_view(["POST"])
def account_signup(request):
    if request.method == "POST":
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사 실패 시 오류 메시지를 반환
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def account_profile(request, username):
    user = get_object_or_404(User, username=username)
#    if request.method == "GET":
    serializer=UserSignupSerializer(user)
    return Response (serializer.data)