from django.shortcuts import render, redirect
from django import views
from .models import UserManager, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import random


from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import serializers

from . import forms

# Create your views here.

def homePage(request):
    return render(request, "core_auth/home.html", {})

class SignUpPage(views.View):
    def get(self, request):
        return render(request, "core_auth/signup.html", {'signup_form': forms.SignUp, 'is_loggdin': False})

    def post(self, request):
        info = request.POST
        files = request.FILES
        print(info, files)
        dir(info)
        try:
            if info['password'] == info['confirm_password']:
                user = User.objects.create_user(email=info['email'], password=info['password'])
                user.first_name, user.last_name, user.age = info['first_name'], info['last_name'], info['age']
                user.profile_pic = files['profile_pic']

                if info['username']:
                    user.username = info['username']
                else:
                    user.username = user.first_name.lower() + user.last_name.lower() + str(random.randint(0, 1000))

                user.save()
                print(user)
            else:
                return render(request, "core_auth/signup.html", {'signup_form': forms.SignUp, 'error_form': "Passwords don't match, please re-enter.", 'is_loggdin': False})

        except Exception as e:
            print(e)
            return render(request, "core_auth/signup.html", {'signup_form': forms.SignUp, 'error_form': e.__str__(), 'is_loggdin': False})


        return render(request, "core_auth/signup.html", {'signup_form': forms.SignUp, 'error_form': 'Registered Successfully!!!', 'color': 'green', 'is_loggdin': False})

class LoginPage(views.View):
    def get(self, request):
        return render(request, "core_auth/login.html", {'login_form': forms.LoginForm, 'is_loggdin': False})
    def post(self, request):
        info = request.POST
        try:
            user = authenticate(request=request, email=info['email'], password=info['password'])
            if user.is_authenticated:
                login(request=request, user=user)
            print(user)
            return redirect('/dashboard/')
        except Exception as e:
            print(e)
            return render(request, "core_auth/login.html", {'login_form': forms.LoginForm, 'error_login': e.__str__(), 'is_loggdin': False})
        return render(request, "core_auth/login.html", {'login_form': forms.LoginForm, 'is_loggdin': False})

class DashboardPage(views.View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        user = request.user
        print(user)
        return render(request, 'core_auth/dashboard.html', {'user_details': user, 'is_loggdin': True})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        return render(request, 'core_auth/dashboard.html', {'user_details': user, 'is_loggdin': True})

@login_required
def Logout(request):
    logout(request)
    return redirect('/login/')


# API Views

class UserDetails(APIView):
    permission_classes = (
        IsAuthenticated,
    )
    def get(self, request):
        user = request.user
        serialized_data = serializers.UserDetailsSerializers(user)
        return Response(data=serialized_data.data)


