from django.db import models
from math import pi, sin, cos, atan2, sqrt


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)


class Route(models.Model):
    type = models.CharField(max_length=40)
    distance = models.FloatField()
    user = models.ForeignKey(User)


    def save(self, *args, **kwargs):
        geopoints = GeoPoint.objects.filter('route')
    def get_distance(self, geo1, geo2):
        radius = 6371  # Radius of the earth in km
        lat1, lon1 = geo1.latitude, geo1.longitude
        lat2, lon2 = geo2.latitude, geo2.longitude
        dlat, dlon = self.deg2rad(lat2 - lat1), self.deg2rad(lon2 - lon1)

        a = sin(dlat/2) * sin(dlat/2) + cos(self.deg2rad(lat1)) * cos(self.deg2rad(lat2)) * sin(dlon/2) * sin(dlon/2)

        c = 2 * atan2(sqrt(a), sqrt(1-a))
        return radius * c  # Distance in km


    def deg2rad(self, deg):
        return deg * (pi/180)


class GeoPoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    sequence_id = models.IntegerField()
    route = models.ForeignKey(Route)



