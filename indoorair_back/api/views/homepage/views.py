from rest_framework import status, response, views
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect


class GetVersion(views.APIView):
    def get(self, request):
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'version': '0.1.0',
            }
        )
# http --form GET http://127.0.0.1:8000/api/version
