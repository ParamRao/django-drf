from rest_framework import serializers
from .models import RoutingUrl


class RoutingUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutingUrl
        fields = "__all__"
