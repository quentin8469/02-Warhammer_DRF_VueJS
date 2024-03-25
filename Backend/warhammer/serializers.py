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

    maitre_du_jeu_username = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerCampagne
        fields = "__all__"

    def get_maitre_du_jeu_username(self, obj):
        return obj.maitre_du_jeu.username if obj.maitre_du_jeu else None


class WarhammerPlayerSerializers(serializers.ModelSerializer):
    """Warhammer Player Serializers"""

    campagne_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerPlayer
        fields = "__all__"

    def get_campagne_actuelle_nom(self, obj):
        return obj.campagne.nom_de_campagne if obj.campagne else None


class WarhammerArmeContactSerializers(serializers.ModelSerializer):
    """Warhammer ArmeContact Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerArmeContact
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerArmeDistanceSerializers(serializers.ModelSerializer):
    """Warhammer ArmeDistance Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerArmeDistance
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerArmureSerializers(serializers.ModelSerializer):
    """Warhammer ArmeDistance Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerArmure
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerBourseSerializers(serializers.ModelSerializer):
    """Warhammer Bourse Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerBourse
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerCaracteristiqueActuelleSerializers(serializers.ModelSerializer):
    """Warhammer CaracteristiqueActuelle Serializers"""

    encombrement_max = serializers.SerializerMethodField()
    deplacement_round = serializers.SerializerMethodField()
    deplacement_tour = serializers.SerializerMethodField()
    deplacement_kmh = serializers.SerializerMethodField()
    initiative_attaque_list_tuple = serializers.SerializerMethodField()
    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerCaracteristiqueActuelle
        fields = "__all__"

    def get_encombrement_max(self, obj):
        return obj.encombrement_max()

    def get_deplacement_round(self, obj):
        return obj.deplacement_round()

    def get_deplacement_tour(self, obj):
        return obj.deplacement_round()

    def get_deplacement_kmh(self, obj):
        return obj.deplacement_round()

    def get_initiative_attaque_list_tuple(self, obj):
        return obj.initiative_attaque_list_tuple()

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerCaracteristiqueBaseSerializers(serializers.ModelSerializer):
    """Warhammer CaracteristiqueBase Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerCaracteristiqueBase
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerCompetenceSerializers(serializers.ModelSerializer):
    """Warhammer Competence Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerCompetence
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerDescriptionPersonnelleSerializers(serializers.ModelSerializer):
    """Warhammer Description Personnelle Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerDescriptionPersonnelle
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerEquipementSerializers(serializers.ModelSerializer):
    """Warhammer Equipement Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerEquipement
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerExperiencePersonnageSerializers(serializers.ModelSerializer):
    """Warhammer ExperiencePersonnage Serializers"""

    xp_total = serializers.SerializerMethodField()
    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerExperiencePersonnage
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None

    def get_xp_total(self, obj):
        return obj.xp_total()


class WarhammerMagieSerializers(serializers.ModelSerializer):
    """Warhammer Magie Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerMagie
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerMontureSerializers(serializers.ModelSerializer):
    """Warhammer Monture Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerMonture
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerPlanCarriereSerializers(serializers.ModelSerializer):
    """WarhammerPlanCarriere Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerPlanCarriere
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerPointDeBlessureSerializers(serializers.ModelSerializer):
    """Warhammer Point De Blessure Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerPointDeBlessure
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None


class WarhammerPointDeDestinSerializers(serializers.ModelSerializer):
    """Warhammer Point De Destin Serializers"""

    pdd_total = serializers.SerializerMethodField()
    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerPointDeDestin
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None

    def get_pdd_total(self, obj):
        return obj.pdd_total()


class WarhammerSortilegeSerializers(serializers.ModelSerializer):
    """Warhammer Sortilege Serializers"""

    personnage_actuelle_nom = serializers.SerializerMethodField()

    class Meta:
        model = WarhammerSortilege
        fields = "__all__"

    def get_personnage_actuelle_nom(self, obj):
        return obj.player.nom if obj.player else None
