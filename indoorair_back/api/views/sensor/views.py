from django.shortcuts import render
from rest_framework import status, views, response
from django.shortcuts import get_object_or_404

from foundation.models import Instrument, Sensor, TimeSeriesDatum
from api.serializers import SensorSerializer


class SensorRetrieveAPI(views.APIView):
    def get_object(self,id):
        return get_object_or_404(Sensor, id=id)


    def get(self, request, id):
        object = self.get_object(id)
        serializer = SensorSerializer(object, many=False)
        return response.Response(
            status = status.HTTP_200_OK,
            data = serializer.data,
        )
