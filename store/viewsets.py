from rest_framework import viewsets

from store.models import Lock
from store.serializers import LockerSerializer


class LockerViewSet(viewsets.ModelViewSet):
    queryset = Lock.objects.all()
    serializer_class = LockerSerializer