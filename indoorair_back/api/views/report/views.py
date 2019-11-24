from django.shortcuts import render
import csv
from django.http import HttpResponse

from foundation.models import TimeSeriesDatum


def download_csv_report_01_temperature_sensor_api(request):
    # Create the HttpResponse object with the appropriate CSV header.

    data = TimeSeriesDatum.objects.filter(
        sensor__name ="Temperature",
        sensor__insturment__user=request.user,
    )

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="temperature_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Sensor_id','time', 'value'])
    for datum in data:
        #header row
        writer.writerow([datum.sensor.id, datum.time,datum.value])


    return response
