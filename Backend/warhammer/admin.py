from django.contrib import admin
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


# Register your models here.
@admin.register(WarhammerCampagne)
class CampagneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nom_de_campagne",
        "date_creation",
        "date_update",
        "date_debut",
        "date_end",
        "image_campagne",
        "maitre_du_jeu",
        "campagne_etat",
    )


@admin.register(WarhammerPlayer)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nom",
        "race",
        "sexe",
        "vocation",
        "alignement",
        "age",
        "taille",
        "poids",
        "cheveux",
        "yeux",
        "photo_personnage",
        "point_destin",
        "debouches",
        "point_folie",
        "langue",
        "note",
        "mort_tuer",
        "date_creation",
        "date_update",
        "joueur",
        "campagne",
    )


@admin.register(WarhammerExperiencePersonnage)
class ExperiencePersonnageAdmin(admin.ModelAdmin):
    list_display = ("id", "xp_actuelle", "xp_depense", "player")


@admin.register(WarhammerDescriptionPersonnelle)
class DescriptionPersonnelleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "lieu_naissance",
        "signe_distinctif",
        "membre_famille",
        "description_perso",
        "player",
    )


@admin.register(WarhammerCaracteristiqueBase)
class CaracteristiqueBaseAdmin(admin.ModelAdmin):
    list_display = (
        "mouvement",
        "capacite_combat",
        "capacité_tir",
        "force",
        "endurance",
        "point_blessure",
        "initiative",
        "nb_attaque",
        "dexterite",
        "commandement",
        "intelligence",
        "calme",
        "force_mentale",
        "sociabilite",
        "player",
    )


@admin.register(WarhammerPlanCarriere)
class PlanCarriereAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "mouvement",
        "capacite_combat",
        "capacité_tir",
        "force",
        "endurance",
        "point_blessure",
        "initiative",
        "nb_attaque",
        "dexterite",
        "commandement",
        "intelligence",
        "calme",
        "force_mentale",
        "sociabilite",
        "player",
    )


@admin.register(WarhammerCaracteristiqueActuelle)
class CaracteristiqueActuelleAdmin(admin.ModelAdmin):
    list_display = (
        "mouvement",
        "capacite_combat",
        "capacité_tir",
        "force",
        "endurance",
        "point_blessure",
        "initiative",
        "nb_attaque",
        "dexterite",
        "commandement",
        "intelligence",
        "calme",
        "force_mentale",
        "sociabilite",
        "player",
    )


@admin.register(WarhammerCompetence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "description",
        "bonus",
        "malus",
        "apprentissage",
        "cout_xp",
        "niveau",
        "player",
    )


@admin.register(WarhammerArmeContact)
class ArmeContactAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "initiative",
        "toucher",
        "degats",
        "parade",
        "encombrement",
        "note",
        "player",
    )


@admin.register(WarhammerArmeDistance)
class ArmeDistanceAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "porte_courte",
        "porte_longue",
        "porte_extreme",
        "force_effective",
        "armer_tirer",
        "encombrement",
        "munitions",
        "nb_munitions",
        "note",
        "player",
    )


@admin.register(WarhammerArmure)
class ArmureAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "protection",
        "localisation",
        "encombrement",
        "note",
        "player",
    )


@admin.register(WarhammerMagie)
class MagieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "point_magie_personnage",
        "point_magie_actuel",
        "point_magie_supplementaire",
        "famillier_personnage",
        "nombre_sort",
        "recuperation_pm",
        "armure_autorisee",
        "arme_non_autorisee",
        "niveau_magique",
        "niveau_pouvoir",
        "note",
        "player",
    )


@admin.register(WarhammerSortilege)
class SortilegeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nom_sortilege",
        "type_magie",
        "niveau_sort",
        "cout_point_magie",
        "porte",
        "duree",
        "degats",
        "composants",
        "description_sort",
        "incantation",
        "apprentissage",
        "cout_xp",
        "note",
        "player",
    )


@admin.register(WarhammerEquipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "quantite",
        "encombrement",
        "note",
        "player",
    )


@admin.register(WarhammerBourse)
class BourseAdmin(admin.ModelAdmin):
    list_display = (
        "couronne",
        "pistole",
        "sous",
        "encombrement",
        "autre",
        "player",
    )


@admin.register(WarhammerMonture)
class MontureAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "mouvement",
        "capacite_combat",
        "capacité_tir",
        "force",
        "endurance",
        "point_blessure",
        "initiative",
        "nb_attaque",
        "dexterite",
        "commandement",
        "intelligence",
        "calme",
        "force_mentale",
        "sociabilite",
        "player",
    )


@admin.register(WarhammerPointDeDestin)
class PointDeDestinAdmin(admin.ModelAdmin):
    list_display = (
        "pdd_actuel",
        "pdd_depense",
        "player",
    )


@admin.register(WarhammerPointDeBlessure)
class PointDeBlessureAdmin(admin.ModelAdmin):
    list_display = (
        "pdb_max",
        "pdb_actuel",
        "nb_blessure",
        "player",
    )
