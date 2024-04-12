from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


from account.serializers import UserLoginSerializer, UserRegistrationSerializer, UserProfileSerializer

@api_view(['POST'])
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
    return render(request, 'account/login.html', context)


#@csrf_exempt
@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Поздравляем, вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('account:login'))
    else:
        serializer = UserRegistrationSerializer()
    return render(request, 'account/registration.html', {'form': serializer})


@api_view(['GET', 'POST'])
@login_required()
def profile(request):
    if request.method == 'POST':
        serializer = UserProfileSerializer(instance=request.user, data=request.data, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect(reverse('account:profile'))
        else:
            print(serializer.errors)
    else:
        serializer = UserProfileSerializer(instance=request.user)

    context = {
        'title': 'Store-Профиль',
        'serializer': serializer,
    }
    return render(request, 'account/profile.html', context)


@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

