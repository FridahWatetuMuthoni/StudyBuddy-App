from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Room, Topic
from .forms import RoomForm, CustomUserCreationForm
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

def register_user(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error happened during registration')
    context = {
        'form':form
    }
    return render(request, 'base/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, f"{username} does not exist")
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, f"incorrect password")

    return render(request, 'base/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') or ''
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )
    topics = Topic.objects.all()
    rooms_count = rooms.count()
    
    context = {
        'rooms':rooms,
        'topics':topics,
        'rooms_count':rooms_count
    }
    
    return render(request, 'base/home.html', context)

def room(request, pk=None):
    room = get_object_or_404(Room, pk=pk)
    room_messages = room.message_set.all()
    context = {
        'room':room,
        'room_messages':room_messages
    }
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'form':form
    }
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def update_room(request, pk=None):
    room = get_object_or_404(Room, pk=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed here')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'room':room,
        'form':form
    }
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def delete_room(request, pk=None):
    room = get_object_or_404(Room, pk=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    context = {
        'obj':room
    }
    return render(request, 'base/delete.html',context)