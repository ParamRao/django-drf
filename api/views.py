from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def home(request):
    api_urls = {
        'POST': '/ping/',
        'GET': '/info/'
    }

    return Response(api_urls)


@api_view(['POST'])
def ping_view(request):
    return Response(request.data)


@api_view(['GET'])
def info_view(request):
    return Response("{'Receiver': 'Cisco is the best!'}")
