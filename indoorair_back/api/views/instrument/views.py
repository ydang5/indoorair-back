from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from foundation.models import Instrument
from rest_framework import status, response, views

from api.serializers import InstrumentSerializer

class InstrumentListAPIView(views.APIView):
    def get(self,request):
        instruments = Instrument.objects.filter(user=request.user).values('name','location','serial_number')

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'instrument list: ': instruments,
            }
    )

# def post_instruments_create_api(request):
#     name = request.POST.get("name")
#     print(name)
#     try:
#         instrument = Instrument.objects.create(
#             name=name,
#             user=request.user
#         )
#         print("INSTRUMENT ID", instrument.id)
#         return JsonResponse({
#          'was_created': True,
#         })
#     except Exception as e:
#         return JsonResponse({
#          'was_created': False,
#          'reason': str(e),
#         })


class InstrumentRetrieveUpdateAPI(views.APIView):
    def get_object(self,id):
        return get_object_or_404(Instrument, id=int(id))


    def get(self, request, id):
        object = self.get_object(id)
        serializer = InstrumentSerializer(object, many=False)
        return response.Response(
            status = status.HTTP_200_OK,
            data = serializer.data,
        )


    def put(self, request, id):
        object = self.get_object(id)
        serializer = InstrumentSerializer(object, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return response.Response(
            status = status.HTTP_200_OK,
            data = serializer.data,
        )
