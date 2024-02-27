from rest_framework.serializers import ModelSerializer
from apps.contacts.models import Contact

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'first_name', 
            'last_name',
            'email', 
            'phone',
            'message',
        ]