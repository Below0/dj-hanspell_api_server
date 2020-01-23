
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from message.models import Text
from message.serializers import *


@api_view(['GET', 'POST'])
def text_list(request):

    def do_after():
        print(timezone.now())

    if request.method == 'GET':
        queryset = Text.objects.all()
        text_serializer = TextSerializer(queryset, many=True)
        return Response(text_serializer.data)
    elif request.method == 'POST':
        text_serializer = TextSerializer(data={'original': request.data['original']})
        if text_serializer.is_valid():
            text_serializer.save()
            response_serial = ResponseSerializer(data={'chat_id': request.data['chat_id'],
                                                       'checked': text_serializer.data['checked'],
                                                       'errors': text_serializer.data['errors']})
            if response_serial.is_valid():
                return Response(JSONRenderer().render(response_serial.data), status=status.HTTP_201_CREATED)
        return Response(text_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detail_text(request, pk):
    try:
        text = Text.objects.get(pk=pk)
    except Text.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TextSerializer(text)
        return Response(serializer.data)
