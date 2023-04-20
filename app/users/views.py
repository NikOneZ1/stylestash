from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import CreateUserSerializer, ResponseUserSerializer
from users.services.auth import generate_tokens


class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens_data = generate_tokens(user)
        return Response(data=tokens_data, status=status.HTTP_201_CREATED)


class MyUserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ResponseUserSerializer

    def get_object(self):
        return self.request.user
