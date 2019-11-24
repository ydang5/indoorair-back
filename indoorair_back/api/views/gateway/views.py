from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, response, views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from api.serializers import LoginSerializer, RegisterSerializer


class LoginAPI(views.APIView):
    def post(self, request):

        login_serializer = LoginSerializer(data = request.data, context={
            'request':request,
        })
        login_serializer.is_valid(raise_exception=True)
        login_serializer.save()

        return response.Response(
            status=status.HTTP_200_OK,
            data = {
                    'message': 'Login successfully.',
                })




class RegisterAPI(views.APIView):

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(
            status = status.HTTP_201_CREATED,
            data = serializer.data,
        )



class LoginAPI(views.APIView):
    def post(self, request):

        login_serializer = LoginSerializer(data = request.data, context={
            'request':request,
        })
        login_serializer.is_valid(raise_exception=True)
        login_serializer.save()

        return response.Response(
            status=status.HTTP_200_OK,
            data = {
                    'message': 'Login successfully.',
                })



class AccountLogoutAPI(views.APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return response.Response(
            status=status.HTTP_200_OK,
            data = {
                'message': 'You have been logged out',
            })

        else:
            return response.Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data = {
                'message': 'Please login first',
        })
