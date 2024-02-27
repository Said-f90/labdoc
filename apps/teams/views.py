from rest_framework.viewsets import ModelViewSet
from apps.teams.models import Team
from apps.teams.serializers import TeamSerializers

class TaemApiViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializers
    