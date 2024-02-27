from rest_framework.routers import DefaultRouter
from apps.certificates.views import CertificateApiViewSet

router = DefaultRouter()
router.register(
    r'certificates',
    CertificateApiViewSet
)

urlpatterns = router.urls