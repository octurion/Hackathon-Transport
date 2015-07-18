from django.db import models
from math import pi, sin, cos, atan2, sqrt


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)


class Route(models.Model):
    user = models.ForeignKey(User)
    type = models.CharField(max_length=40)


class GeoPoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    sequence_id = models.IntegerField()
    route = models.ForeignKey(Route)


def get_distance(geo1, geo2):
    radius = 6371  # Radius of the earth in km
    lat1, lon1 = geo1.latitude, geo1.longitude
    lat2, lon2 = geo2.latitude, geo2.longitude
    dlat, dlon = deg2rad(lat2 - lat1), deg2rad(lon2 - lon1)

    a = sin(dlat/2) * sin(dlat/2) + cos(deg2rad(lat1)) * cos(deg2rad(lat2)) * sin(dlon/2) * sin(dlon/2)

    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return radius * c  # Distance in km


def deg2rad(deg):
    return deg * (pi/180)
