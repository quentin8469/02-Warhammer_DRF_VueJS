from django.shortcuts import render
from rest_framework import viewsets
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
from warhammer.serializers import (
    WarhammerCampagneSerializers,
    WarhammerPlayerSerializers,
    WarhammerArmeContactSerializers,
    WarhammerArmeDistanceSerializers,
    WarhammerArmureSerializers,
    WarhammerBourseSerializers,
    WarhammerCaracteristiqueActuelleSerializers,
    WarhammerCaracteristiqueBaseSerializers,
    WarhammerCompetenceSerializers,
    WarhammerDescriptionPersonnelleSerializers,
    WarhammerEquipementSerializers,
    WarhammerExperiencePersonnageSerializers,
    WarhammerMagieSerializers,
    WarhammerMontureSerializers,
    WarhammerPlanCarriereSerializers,
    WarhammerPointDeBlessureSerializers,
    WarhammerPointDeDestinSerializers,
    WarhammerSortilegeSerializers,
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


class WarhammerArmeContactViewSet(viewsets.ModelViewSet):
    """Warhammer ArmeContact API View"""

    queryset = WarhammerArmeContact.objects.all()
    serializer_class = WarhammerArmeContactSerializers


class WarhammerArmeDistanceViewSet(viewsets.ModelViewSet):
    """Warhammer ArmeDistance API View"""

    queryset = WarhammerArmeDistance.objects.all()
    serializer_class = WarhammerArmeDistanceSerializers


class WarhammerArmureViewSet(viewsets.ModelViewSet):
    """Warhammer Armure API View"""

    queryset = WarhammerArmure.objects.all()
    serializer_class = WarhammerArmureSerializers


class WarhammerBourseViewSet(viewsets.ModelViewSet):
    """Warhammer Bourse API View"""

    queryset = WarhammerBourse.objects.all()
    serializer_class = WarhammerBourseSerializers


class WarhammerCaracteristiqueActuelleViewSet(viewsets.ModelViewSet):
    """Warhammer Caracteristique Actuelle API View"""

    queryset = WarhammerCaracteristiqueActuelle.objects.all()
    serializer_class = WarhammerCaracteristiqueActuelleSerializers


class WarhammerCaracteristiqueBaseViewSet(viewsets.ModelViewSet):
    """Warhammer Caracteristique Base API View"""

    queryset = WarhammerCaracteristiqueBase.objects.all()
    serializer_class = WarhammerCaracteristiqueBaseSerializers


class WarhammerCompetenceViewSet(viewsets.ModelViewSet):
    """Warhammer Competence API View"""

    queryset = WarhammerCompetence.objects.all()
    serializer_class = WarhammerCompetenceSerializers


class WarhammerDescriptionPersonnelleViewSet(viewsets.ModelViewSet):
    """Warhammer Description Personnelle API View"""

    queryset = WarhammerDescriptionPersonnelle.objects.all()
    serializer_class = WarhammerDescriptionPersonnelleSerializers


class WarhammerEquipementViewSet(viewsets.ModelViewSet):
    """WarhammerEquipement API View"""

    queryset = WarhammerEquipement.objects.all()
    serializer_class = WarhammerEquipementSerializers


class WarhammerExperiencePersonnageViewSet(viewsets.ModelViewSet):
    """Warhammer Experience Personnage API View"""

    queryset = WarhammerExperiencePersonnage.objects.all()
    serializer_class = WarhammerExperiencePersonnageSerializers


class WarhammerMagieViewSet(viewsets.ModelViewSet):
    """Warhammer Magie API View"""

    queryset = WarhammerMagie.objects.all()
    serializer_class = WarhammerMagieSerializers


class WarhammerMontureViewSet(viewsets.ModelViewSet):
    """Warhammer Monture API View"""

    queryset = WarhammerMonture.objects.all()
    serializer_class = WarhammerMontureSerializers


class WarhammerPlanCarriereViewSet(viewsets.ModelViewSet):
    """Warhammer Plan Carriere API View"""

    queryset = WarhammerPlanCarriere.objects.all()
    serializer_class = WarhammerPlanCarriereSerializers


class WarhammerPointDeBlessureViewSet(viewsets.ModelViewSet):
    """Warhammer Point De Blessure API View"""

    queryset = WarhammerPointDeBlessure.objects.all()
    serializer_class = WarhammerPointDeBlessureSerializers


class WarhammerPointDeDestinViewSet(viewsets.ModelViewSet):
    """Warhammer Point De Destin API View"""

    queryset = WarhammerPointDeDestin.objects.all()
    serializer_class = WarhammerPointDeDestinSerializers


class WarhammerSortilegeViewSet(viewsets.ModelViewSet):
    """Warhammer Sortilege API View"""

    queryset = WarhammerSortilege.objects.all()
    serializer_class = WarhammerSortilegeSerializers
