from rest_framework import response, views, status


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
