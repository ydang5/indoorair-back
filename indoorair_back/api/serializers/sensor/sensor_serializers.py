from rest_framework import serializers


class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
