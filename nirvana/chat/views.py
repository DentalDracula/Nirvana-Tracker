from django.shortcuts import render
from .models import Message, Room
from django.contrib.auth.decorators import login_required
#--------------------------community---------------------------------
@login_required
def community(request):
    rooms = Room.objects.all()
    return render(request, 'community.html',{'rooms':rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room.html',{'room':room, 'messages':messages})
 