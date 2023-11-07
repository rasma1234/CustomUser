from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import *
from .models import Post
from .serializers import CustomUserSerializer, PostSerializer
# Create your views here.

# class CustomUserListAPIView(ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomUserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
    

class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    