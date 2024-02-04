from django.urls import path
from .views import CreateRoom, ListRooms

urlpatterns = [
    path('create', CreateRoom.as_view()),
    path('', ListRooms.as_view()),
]
