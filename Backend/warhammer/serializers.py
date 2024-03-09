from rest_framework import serializers
from warhammer.models import WarhammerCampagne, WarhammerPlayer


class WarhammerCampagneSerializers(serializers.ModelSerializer):
    """Warhammer Camapagne Serializers"""

    class Meta:
        model = WarhammerCampagne
        fields = "__all__"


class WarhammerPlayerSerializers(serializers.ModelSerializer):
    """Warhammer Player Serializers"""

    class Meta:
        model = WarhammerPlayer
        fields = "__all__"
