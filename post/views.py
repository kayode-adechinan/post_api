from django.shortcuts import render
from rest_framework import viewsets
from post.models import  Post
from post.serializers import  PostSerializer
# Create your views here.


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        serializer.save(picture='http://via.placeholder.com/350x150')