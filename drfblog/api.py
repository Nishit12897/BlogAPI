from rest_framework import generics
from rest_framework.response import Response
from .serializer import *

from .models import Blog


class BlogCreateApi(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogPostSerializer

class BlogListApi(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogPostSerializer

class BlogUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogPostSerializer

# class BlogDeleteApi(generics.DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogPostSerializer
