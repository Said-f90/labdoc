from rest_framework.routers import DefaultRouter
from apps.teams.views import TaemApiViewSet

router = DefaultRouter()

router.register(
    r'teams',
    TaemApiViewSet
)

urlpatterns = router.urls