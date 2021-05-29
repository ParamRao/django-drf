from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.http.response import JsonResponse
from rest_framework import status
from api.models import RoutingUrl
from api.serializers import RoutingUrlSerializer


# Create your views here.
@swagger_auto_schema(methods=['POST'], request_body=RoutingUrlSerializer,
                     operation_description="Post URL Ping Detail; Accepts a body containing a url key and "
                                           "corresponding link, ie `{‘url’: ‘ https://www.foobar.com‘}`;")
@api_view(['POST'])
def ping_view(request):
    """
    Save the ping data posted to db
    :param: request
    :return: json response data
    """
    ping_serializer = RoutingUrlSerializer(data=request.data)
    if ping_serializer.is_valid():
        ping_serializer.save()
        return JsonResponse(ping_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(ping_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['GET'], operation_description='Returns hardcoded status of '
                                                            '`{“Receiver”: “Cisco is the best!”}`')
@api_view(['GET'])
def info_view(request):
    """
    Send hardcoded response
    :param: request
    :return: json response data
    """
    return Response("{'Receiver': 'Cisco is the best!'}")


@swagger_auto_schema(methods=['GET'], operation_description="List all the ping details posted")
@api_view(['GET'])
def list_ping_view(request):
    """
    List the ping data saved in db
    :param: request
    :return: json response data
    """
    ping_list = RoutingUrl.objects.all()
    ping_serializer = RoutingUrlSerializer(ping_list, many=True)
    return Response(ping_serializer.data)
