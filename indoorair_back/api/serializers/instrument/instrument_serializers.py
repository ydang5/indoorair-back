from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from foundation.models import Instrument, Sensor, TimeSeriesDatum


class InstrumentSerializer(serializers.Serializer):


    id = serializers.IntegerField(read_only=True)
    location = serializers.CharField()
    serial_number = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)

    # def create(self, validated_data):
    #
    #     location = validated_data.get('location', None)
    #     instrument = Instrument.objects.create(location=location)
    #     return instrument


    def update(self, object, validated_data):
        location = validated_data.get('location', None)
        name = validated_data.get('name',None)
        object.name=name
        object.location = location
        object.save()
        return object
