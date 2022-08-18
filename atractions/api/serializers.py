from rest_framework.serializers import ModelSerializer
from atractions.models import Atractions

class AtractionsSerializer(ModelSerializer):
    class Meta:
        model = Atractions
        fields = ('id', 'name', 'description', 'working_time', 'min_age', 'foto')