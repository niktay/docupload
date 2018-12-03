from api.models import Confidentiality
from api.models import FileType
from api.serializers import ConfidentialitySerializer
from api.serializers import FileTypeSerializer
from rest_framework import viewsets


class ConfidentialityViewSet(viewsets.ModelViewSet):
    queryset = Confidentiality.objects.all()
    serializer_class = ConfidentialitySerializer


class FileTypeViewSet(viewsets.ModelViewSet):
    queryset = FileType.objects.all()
    serializer_class = FileTypeSerializer
