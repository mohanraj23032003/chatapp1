from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.


def room(request, my_room):
    return render(request, "chat/room.html",{
                  "room_name" : my_room
                  })
