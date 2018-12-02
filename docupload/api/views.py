from api.models import Confidentiality
from api.serializers import ConfidentialitySerializer
from rest_framework import viewsets


class ConfidentialityViewSet(viewsets.ModelViewSet):
    queryset = Confidentiality.objects.all()
    serializer_class = ConfidentialitySerializer
