from rest_framework.serializers import ModelSerializer
from apps.teams.models import Team

class TeamSerializers(ModelSerializer):
    class Meta:
        model = Team
        fields = [ 
            'id',
            'first_name',
            'last_name',
            'position',
            'phone', 
            'photo'
        ]