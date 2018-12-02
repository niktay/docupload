from api.models import Confidentiality
from rest_framework import serializers


class ConfidentialitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Confidentiality
        fields = ('name',)
