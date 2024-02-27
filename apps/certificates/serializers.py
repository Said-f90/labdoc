from rest_framework.serializers import ModelSerializer
from apps.certificates.models import Certificate

class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            'id',
            'title', 
            'description',
            'photo',
        ]