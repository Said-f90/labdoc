from rest_framework.viewsets import ModelViewSet
from apps.homes.models import Laborotory
from apps.homes.serilizers import LaborotorySerializer

class LaborotoryApiViewSet(ModelViewSet):
    queryset = Laborotory.objects.all()
    serializer_class = LaborotorySerializer

 