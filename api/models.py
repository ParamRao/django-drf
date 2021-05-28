from django.db import models


# Create your models here.
class RoutingUrl(models.Model):
    url = models.TextField()
