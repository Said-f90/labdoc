from rest_framework.routers import DefaultRouter
from apps.partners.views import PartnerApiViewSet

router = DefaultRouter()

router.register(
    r'partners',
    PartnerApiViewSet
)

urlpatterns = router.urls
