from rest_framework.routers import DefaultRouter
from apps.homes.views import LaborotoryApiViewSet

router = DefaultRouter()


router.register(
    r'homes',
    LaborotoryApiViewSet
)

urlpatterns = router.urls