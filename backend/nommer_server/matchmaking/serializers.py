from rest_framework.serializers import ModelSerializer
from .models import Party

class PartySerial(ModelSerializer):

    class Meta:
        model = Party
        fields = ('id','host', 'response')