from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer


class CreateRoom(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListRooms(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
