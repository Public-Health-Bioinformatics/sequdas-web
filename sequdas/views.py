from rest_framework import viewsets
from sequdas import models
from sequdas import serializers

class SequencerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sequencer.objects.all()
    serializer_class = serializers.SequencerSerializer

class SequenceRunViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SequenceRun.objects.all()
    serializer_class = serializers.SequenceRunPolymorphicSerializer

class MiseqSampleSheetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MiseqSampleSheet.objects.all()
    serializer_class = serializers.MiseqSampleSheetSerializer
