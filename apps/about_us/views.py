from rest_framework.viewsets import ModelViewSet
from apps.about_us.models import About
from apps.about_us.serializers import AboutSerializer

class AboutApiViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer