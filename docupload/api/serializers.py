from api.models import Confidentiality
from api.models import FileType
from rest_framework import serializers


class ConfidentialitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Confidentiality
        fields = ('name',)


class FileTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FileType
        fields = ('name',)
