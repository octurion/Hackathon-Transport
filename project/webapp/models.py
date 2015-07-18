from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
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
