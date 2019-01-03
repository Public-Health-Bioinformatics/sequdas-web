from rest_framework import serializers
from sequdas import models

class SampleSheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SampleSheet
        fields = '__all__'
        
class SequenceRunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SequenceRun
        fields = '__all__'

class ReadSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ReadSummary
        fields = '__all__'

class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Sample
        fields = '__all__'
