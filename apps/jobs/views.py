from rest_framework.viewsets import ModelViewSet
from apps.jobs.models import Job
from apps.jobs.serializers import Jobserializer

class JobApiViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = Jobserializer