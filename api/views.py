from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
@api_view(['GET'])
def home(request):
    api_urls = {
        'ENDPOINT1': '/ping/',
        'ENDPOINT2': '/info/',
        'ENDPOINT3': '/swagger/'
    }

    return Response(api_urls)


@swagger_auto_schema(methods=['POST'],
                     request_body=openapi.Schema(
                         type=openapi.TYPE_OBJECT,
                         properties={
                             'url': openapi.Schema(type=openapi.TYPE_STRING,
                                                   description='url mapping; Example: "url": "http://fooexample.com"')
                         }))
@api_view(['POST'])
def ping_view(request):
    return Response(request.data)


@api_view(['GET'])
def info_view(request):
    return Response("{'Receiver': 'Cisco is the best!'}")
