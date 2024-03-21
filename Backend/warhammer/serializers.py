from rest_framework import serializers
from warhammer.models import (
    WarhammerCampagne,
    WarhammerPlayer,
    WarhammerArmeContact,
    WarhammerArmeDistance,
    WarhammerArmure,
    WarhammerBourse,
    WarhammerCaracteristiqueActuelle,
    WarhammerCaracteristiqueBase,
    WarhammerCompetence,
    WarhammerDescriptionPersonnelle,
    WarhammerEquipement,
    WarhammerExperiencePersonnage,
    WarhammerMagie,
    WarhammerMonture,
    WarhammerPlanCarriere,
    WarhammerPointDeBlessure,
    WarhammerPointDeDestin,
    WarhammerSortilege,
)


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


class WarhammerArmeContactSerializers(serializers.ModelSerializer):
    """Warhammer ArmeContact Serializers"""

    class Meta:
        model = WarhammerArmeContact
        fields = "__all__"


class WarhammerArmeDistanceSerializers(serializers.ModelSerializer):
    """Warhammer ArmeDistance Serializers"""

    class Meta:
        model = WarhammerArmeDistance
        fields = "__all__"


class WarhammerArmureSerializers(serializers.ModelSerializer):
    """Warhammer ArmeDistance Serializers"""

    class Meta:
        model = WarhammerArmure
        fields = "__all__"


class WarhammerBourseSerializers(serializers.ModelSerializer):
    """Warhammer Bourse Serializers"""

    class Meta:
        model = WarhammerBourse
        fields = "__all__"


class WarhammerCaracteristiqueActuelleSerializers(serializers.ModelSerializer):
    """Warhammer CaracteristiqueActuelle Serializers"""

    class Meta:
        model = WarhammerCaracteristiqueActuelle
        fields = "__all__"


class WarhammerCaracteristiqueBaseSerializers(serializers.ModelSerializer):
    """Warhammer CaracteristiqueBase Serializers"""

    class Meta:
        model = WarhammerCaracteristiqueBase
        fields = "__all__"


class WarhammerCompetenceSerializers(serializers.ModelSerializer):
    """Warhammer Competence Serializers"""

    class Meta:
        model = WarhammerCompetence
        fields = "__all__"


class WarhammerDescriptionPersonnelleSerializers(serializers.ModelSerializer):
    """Warhammer Description Personnelle Serializers"""

    class Meta:
        model = WarhammerDescriptionPersonnelle
        fields = "__all__"


class WarhammerEquipementSerializers(serializers.ModelSerializer):
    """Warhammer Equipement Serializers"""

    class Meta:
        model = WarhammerEquipement
        fields = "__all__"


class WarhammerExperiencePersonnageSerializers(serializers.ModelSerializer):
    """Warhammer ExperiencePersonnage Serializers"""

    class Meta:
        model = WarhammerExperiencePersonnage
        fields = "__all__"


class WarhammerMagieSerializers(serializers.ModelSerializer):
    """Warhammer Magie Serializers"""

    class Meta:
        model = WarhammerMagie
        fields = "__all__"


class WarhammerMontureSerializers(serializers.ModelSerializer):
    """Warhammer Monture Serializers"""

    class Meta:
        model = WarhammerMonture
        fields = "__all__"


class WarhammerPlanCarriereSerializers(serializers.ModelSerializer):
    """WarhammerPlanCarriere Serializers"""

    class Meta:
        model = WarhammerPlanCarriere
        fields = "__all__"


class WarhammerPointDeBlessureSerializers(serializers.ModelSerializer):
    """Warhammer Point De Blessure Serializers"""

    class Meta:
        model = WarhammerPointDeBlessure
        fields = "__all__"


class WarhammerPointDeDestinSerializers(serializers.ModelSerializer):
    """Warhammer Point De Destin Serializers"""

    class Meta:
        model = WarhammerPointDeDestin
        fields = "__all__"


class WarhammerSortilegeSerializers(serializers.ModelSerializer):
    """Warhammer Sortilege Serializers"""

    class Meta:
        model = WarhammerSortilege
        fields = "__all__"
