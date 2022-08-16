from rest_framework.viewsets import ModelViewSet
from atractions.models import Atractions
from .serializers import AtractionsSerializer

class AtractionsViewSet(ModelViewSet):
    queryset = Atractions.objects.all()
    serializer_class = AtractionsSerializer