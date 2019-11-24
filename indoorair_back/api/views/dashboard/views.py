from rest_framework import status, views, response
from django.shortcuts import get_object_or_404

from foundation.models import Instrument, Sensor, TimeSeriesDatum
from api.serializers import DashboardSerializer

class DashboardAPI(views.APIView):
    def get(self, request):
        instruments = Instrument.objects.filter(user=request.user)
        serializer = DashboardSerializer(instruments)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
