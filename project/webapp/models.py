from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)


class Route(models.Model):
    type = models.CharField(max_length=40)
    distance = models.FloatField()
    user = models.ForeignKey(User)


class GeoPoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    sequence_id = models.IntegerField()
    route = models.ForeignKey(Route)



