from django.shortcuts import render

# Create your views here.
from django_logic.state import State

from rest_framework.response import Response
from rest_framework import generics

from store.models import Lock
from store.serializers import LockerSerializer


class LockerAPIView(generics.ListCreateAPIView):
    serializer_class = LockerSerializer

    def list(self, request, *args, **kwargs):
        query = Lock.objects.all()
        serializer = LockerSerializer(query, many=True)
        return Response(
            serializer.data
        )

    def create(self, request, *args, **kwargs):
        id = request.data['id']
        query = Lock.objects.get(id=id)
        query.status = 'locked'
        query.save(update_fields=['status'])
        serializer = LockerSerializer(query)
        return Response(
            serializer.data
        )
