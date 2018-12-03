from api.models import Confidentiality
from api.models import FileType
from api.models import Language
from api.serializers import ConfidentialitySerializer
from api.serializers import FileTypeSerializer
from api.serializers import LanguageSerializer
from rest_framework import viewsets


class ConfidentialityViewSet(viewsets.ModelViewSet):
    queryset = Confidentiality.objects.all()
    serializer_class = ConfidentialitySerializer


class FileTypeViewSet(viewsets.ModelViewSet):
    queryset = FileType.objects.all()
    serializer_class = FileTypeSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
