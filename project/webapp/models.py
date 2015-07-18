from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Route(models.Model):
    type = models.CharField(max_length=40)
    distance = models.FloatField()
    user = models.ForeignKey(UserProfile)


class GeoPoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    sequence_id = models.IntegerField()
    route = models.ForeignKey(Route)



