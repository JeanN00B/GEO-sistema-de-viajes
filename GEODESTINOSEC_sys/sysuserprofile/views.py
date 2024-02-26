from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, views
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.urls import reverse

'''
class LoginView(View):
    def get(self, request):
        return render(request, 'sysuserprofile/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'sysuserprofile/logged.html', {'user': user})
        else:
            return HttpResponse('Invalid credentials')
'''


'''
class LogoutView:
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Logged out successfully')
            return redirect(reverse('core:index'))
'''