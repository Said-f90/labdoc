from rest_framework.serializers import ModelSerializer
from apps.partners.models import Partner

class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            'id', 
            'title',
            'description',
            'photo',
        ]