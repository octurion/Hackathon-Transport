from rest_framework import serializers

from webapp.models import User
from webapp.models import Route
from webapp.models import GeoPoint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('user')

class GeoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPoint
        fields = ('latitude', 'longitude', 'timestamp', 'sequence_id', 'route')
