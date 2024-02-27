from rest_framework.viewsets import ModelViewSet
from apps.certificates.models import Certificate
from apps.certificates.serializers import CertificateSerializer

class CertificateApiViewSet(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer