from rest_framework import routers
from account.views import AccountCustomUserViewSet

router = routers.DefaultRouter()
router.register("AccountCustomUserViewSet", AccountCustomUserViewSet)
urlpatterns = router.urls
