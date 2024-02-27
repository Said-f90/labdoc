from rest_framework.serializers import ModelSerializer
from apps.jobs.models import Job

class Jobserializer(ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'description'
        ]


        