from rest_framework.serializers import ModelSerializer
from apps.homes.models import Laborotory

class LaborotorySerializer(ModelSerializer):
    class Meta:
        model = Laborotory
        fields = [
            'id',
            'description',
            'plans'
        ]