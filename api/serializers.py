from collections import OrderedDict
from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class NonNullHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, instance):
        result = super(NonNullHyperlinkedModelSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])

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

class MiseqSampleSerializer(NonNullHyperlinkedModelSerializer):
    class Meta:
        model = models.MiseqSample
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'miseqsample-detail', 'lookup_field': 'pk'},
        }
        
class MiseqSampleSheetSerializer(serializers.HyperlinkedModelSerializer):
    samples = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'miseqsample-detail'
    )
    class Meta:
        model = models.MiseqSampleSheet
        fields = (
            'path',
            'iem_file_version',
            'investigator_name',
            'project_name',
            'experiment_name',
            'date',
            'workflow',
            'assay',
            'description',
            'chemistry',
            'application',
            'reverse_complement',
            'adapter',
            'adapter_read2',
            'read1_length',
            'read2_length',
            'samples',
        )
        extra_kwargs = {
            'url': {'view_name': 'miseqsamplesheet-detail', 'lookup_field': 'pk'},
        }

class MiseqSequenceRunSerializer(serializers.HyperlinkedModelSerializer):
    samplesheet = serializers.HyperlinkedRelatedField(
        many = False,
        read_only = True,
        view_name = 'miseqsamplesheet-detail'
    )
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

