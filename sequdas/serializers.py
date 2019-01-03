from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from sequdas import models

class SequencerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sequencer
        fields = '__all__'

class MiseqSampleSheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MiseqSampleSheet
        fields = '__all__'
        
class SequenceRunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SequenceRun
        fields = (
            'run_id',
            'sequencer',
        )

class MiseqSequenceRunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MiseqSequenceRun
        fields = (
            'run_id',
            'sequencer',
            'sample_sheet',
            'folder',
            'cluster_density',
            'clusters_passed_filter_percent',
            'reads_total',
            'reads_passed_filter',
            'bases_greater_than_q30_percent',
        )
        extra_kwargs = {
            'url': {'view_name': 'sequencerun-detail', 'lookup_field': 'pk'},
        }

class MinionSequenceRunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MinionSequenceRun
        fields = (
            'run_id',
            'sequencer',
            'reads_total',
        )
        extra_kwargs = {
            'url': {'view_name': 'sequencerun-detail', 'lookup_field': 'pk'},
        }

class SequenceRunPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        models.SequenceRun: SequenceRunSerializer,
        models.MiseqSequenceRun: MiseqSequenceRunSerializer,
        models.MinionSequenceRun: MinionSequenceRunSerializer
    }

class ReadSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MiseqReadSummary
        fields = '__all__'

class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sample
        fields = '__all__'
