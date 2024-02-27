from rest_framework.routers import DefaultRouter
from apps.jobs.views import JobApiViewSet

router = DefaultRouter()

router.register(
    r'jobs',
    JobApiViewSet
)

urlpatterns = router.urls