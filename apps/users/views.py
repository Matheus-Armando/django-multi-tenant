from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all()
    return JsonResponse({'users': list(users.values())})

def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return JsonResponse({'user': {'id': user.id, 'username': user.username}})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def register_user(request):
    if request.method == 'POST':
        # Logic for user registration goes here
        pass
    return JsonResponse({'message': 'User registration endpoint'})