from api.models import Confidentiality
from api.models import FileType
from api.models import Language
from rest_framework import serializers


class ConfidentialitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Confidentiality
        fields = ('name',)


class FileTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FileType
        fields = ('name',)


class LanguageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Language
        fields = ('name', 'short',)
