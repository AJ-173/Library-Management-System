from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.http import JsonResponse

def admin_signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = AdminUser.objects.create_user(email=email, password=password)
        return JsonResponse({"message": "Admin Created"}, status=201)
    return render(request, 'signup.html')

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Logged in successfully"})
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=400)

def admin_logout(request):
    logout(request)
    return JsonResponse({"message": "Logged out successfully"})
