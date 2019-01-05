from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'groups',
        )

class SequencerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sequencer
        fields = '__all__'

class MiseqSampleSheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MiseqSampleSheet
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'miseqsamplesheet-detail', 'lookup_field': 'pk'},
        }

class MiseqSequenceRunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MiseqSequenceRun
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'miseqsequencerun-detail', 'lookup_field': 'pk'},
        }

class ReadSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MiseqReadSummary
        fields = '__all__'

class MiseqSampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MiseqSample
        fields = '__all__'
