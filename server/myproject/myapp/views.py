from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already taken'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return JsonResponse({'username': username})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
