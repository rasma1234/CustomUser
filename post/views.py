from django.shortcuts import render
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly # new
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
    permission_classes = (IsAuthorOrReadOnly, )
    #queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author= self.request.user)

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
