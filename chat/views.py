from django.shortcuts import render


# Create your views here.



def chat(request):
    return render(request , template_name="index.html")


def room(request , room_name):
    return render(request , "room.html" , context={"room_name" : room_name })


