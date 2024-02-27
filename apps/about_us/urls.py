from rest_framework.routers import DefaultRouter
from apps.about_us.views import AboutApiViewSet

router = DefaultRouter()
router.register(
    r'about_us', 
    AboutApiViewSet
)

urlpatterns = router.urls