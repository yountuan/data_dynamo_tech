from django.shortcuts import render

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from account.serializers import UserLoginSerializer, UserRegistrationSerializer, UserProfileSerializer
from account.models import User

def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        serializer = UserLoginSerializer()
    context = {'serializer': serializer}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Поздравляем, вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        serializer = UserRegistrationSerializer()
    context = {'serializer': serializer}
    return render(request, 'users/registration.html', context)

@login_required()
def profile(request):
    if request.method == 'POST':
        serializer = UserProfileSerializer(instance=request.user, data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(serializer.errors)
    else:
        serializer = UserProfileSerializer(instance=request.user)

    context = {
        'title': 'Store-Профиль',
        'serializer': serializer,
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
