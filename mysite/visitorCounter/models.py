from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()
    ratings = GenericRelation(Rating, null=True, blank=True)

    def __str__(self):
        return self.ip_address


# IPAddress.objects.filter(ratings__isnull=False).order_by('ratings__average')


class MyResume(models.Model):
    title = models.CharField(max_length=150, default='parham')

    def __str__(self):
        return self.title

# class Foo(models.Model):
#     bar = models.CharField(max_length=100)
#     ratings = GenericRelation(Rating, related_query_name='foos')
#
#
# Foo.objects.filter(ratings__isnull=False).order_by('ratings__average')
