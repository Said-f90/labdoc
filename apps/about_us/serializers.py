from rest_framework.serializers import ModelSerializer
from apps.about_us.models import About

class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = [
            'id',
            'title', 
            'description'
        ]
                