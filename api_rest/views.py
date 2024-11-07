from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, UserTasks
from .serializers import UserSerializer, UserTaskSerializer
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Página de sucesso
def user_success_page(request):
    return render(request, 'success.html')

# Página de registro de usuário
def user_registration_page(request):
    if request.method == "POST":
        user_email = request.POST.get("user_email")
        user_password = request.POST.get("user_password")
        user_nickname = request.POST.get('user_nickname')

        # Verificar duplicidade de e-mail
        if User.objects.filter(user_email=user_email).exists():
            messages.error(request, "Já existe um usário com este e-mail. Por favor, use outro e-mail.")
            return redirect('register')
        if User.objects.filter(user_nickname=user_nickname).exists():
            messages.error(request, "Já existe um usário com este nome. Por favor, use outro nome.")
            return redirect('register')
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('success')
        else:
            messages.error(request, "Erro ao registrar o usuário. Por favor, verifique os dados e tente novamente.")

    return render(request, 'register_user.html')


def user_list(request):
    users = User.objects.all() 
    return render(request, 'user_list.html', {'users': users})





# Obter usuário por apelido (nickname)
@api_view(['GET', 'PUT'])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(user_nickname=nick)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Gerenciar usuários
@api_view(['GET'])
def user_manager(request):
    user_nickname = request.GET.get('user', None)
    if user_nickname:
        try:
            user = User.objects.get(user_nickname=user_nickname)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Criar novo usuário
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Atualizar dados de usuário
@api_view(['PUT'])
def update_user(request):
    nickname = request.data.get('user_nickname')
    try:
        updated_user = User.objects.get(user_nickname=nickname)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(updated_user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deletar usuário
@api_view(['DELETE'])
def delete_user(request):    
    nickname = request.data.get('user_nickname')
    try:
        user_to_delete = User.objects.get(user_nickname=nickname)
        user_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def login_page(request):
    if request.method == 'POST':
        user_nickname = request.POST.get('user_nickname')
        user_password = request.POST.get('user_password')
        
        user = authenticate(user_nickname=user_nickname, user_password=user_password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('success')
        else:
            messages.error(request, 'Login inválido. Por favor, tente novamente.')
    return render(request, 'login.html')

def logout_page(request):
    return render(request, 'login.html')