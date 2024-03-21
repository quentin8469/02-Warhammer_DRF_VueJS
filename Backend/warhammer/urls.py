from rest_framework import routers
from warhammer.views import (
    WarhammerCampagneViewSet,
    WarhammerPlayerViewSet,
    WarhammerArmeContactViewSet,
    WarhammerArmeDistanceViewSet,
    WarhammerArmureViewSet,
    WarhammerBourseViewSet,
    WarhammerCaracteristiqueActuelleViewSet,
    WarhammerCaracteristiqueBaseViewSet,
    WarhammerCompetenceViewSet,
    WarhammerDescriptionPersonnelleViewSet,
    WarhammerEquipementViewSet,
    WarhammerExperiencePersonnageViewSet,
    WarhammerMagieViewSet,
    WarhammerMontureViewSet,
    WarhammerPlanCarriereViewSet,
    WarhammerPointDeBlessureViewSet,
    WarhammerPointDeDestinViewSet,
    WarhammerSortilegeViewSet,
)

router = routers.DefaultRouter()
router.register("WarhammerCampagneViewSet", WarhammerCampagneViewSet)
router.register("WarhammerPlayerViewSet", WarhammerPlayerViewSet)
router.register("WarhammerArmeContactViewSet", WarhammerArmeContactViewSet)
router.register("WarhammerArmeDistanceViewSet", WarhammerArmeDistanceViewSet)
router.register("WarhammerArmureViewSet", WarhammerArmureViewSet)
router.register("WarhammerBourseViewSet", WarhammerBourseViewSet)
router.register(
    "WarhammerCaracteristiqueActuelleViewSet", WarhammerCaracteristiqueActuelleViewSet
)
router.register(
    "WarhammerCaracteristiqueBaseViewSet", WarhammerCaracteristiqueBaseViewSet
)
router.register("WarhammerCompetenceViewSet", WarhammerCompetenceViewSet)
router.register(
    "WarhammerDescriptionPersonnelleViewSet", WarhammerDescriptionPersonnelleViewSet
)
router.register("WarhammerEquipementViewSet", WarhammerEquipementViewSet)
router.register(
    "WarhammerExperiencePersonnageViewSet", WarhammerExperiencePersonnageViewSet
)
router.register("WarhammerMagieViewSet", WarhammerMagieViewSet)
router.register("WarhammerMontureViewSet", WarhammerMontureViewSet)
router.register("WarhammerPlanCarriereViewSet", WarhammerPlanCarriereViewSet)
router.register("WarhammerPointDeBlessureViewSet", WarhammerPointDeBlessureViewSet)
router.register("WarhammerPointDeDestinViewSet", WarhammerPointDeDestinViewSet)
router.register("WarhammerSortilegeViewSet", WarhammerSortilegeViewSet)

urlpatterns = router.urls
