from django.shortcuts import render
from rest_framework import viewsets
from warhammer.models import WarhammerCampagne, WarhammerPlayer
from warhammer.serializers import (
    WarhammerCampagneSerializers,
    WarhammerPlayerSerializers,
)


# Create your views here.
class WarhammerCampagneViewSet(viewsets.ModelViewSet):
    """Warhammer Campagne API View"""

    queryset = WarhammerCampagne.objects.all()
    serializer_class = WarhammerCampagneSerializers


class WarhammerPlayerViewSet(viewsets.ModelViewSet):
    """Warhammer Player API View"""

    queryset = WarhammerPlayer.objects.all()
    serializer_class = WarhammerPlayerSerializers
