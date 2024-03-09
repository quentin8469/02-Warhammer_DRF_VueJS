from rest_framework import routers
from warhammer.views import WarhammerCampagneViewSet, WarhammerPlayerViewSet

router = routers.DefaultRouter()
router.register("WarhammerCampagneViewSet", WarhammerCampagneViewSet)
router.register("WarhammerPlayerViewSet", WarhammerPlayerViewSet)

urlpatterns = router.urls
