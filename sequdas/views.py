from rest_framework import viewsets
from sequdas import models
from sequdas import serializers

class SequenceRunViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SequenceRun.objects.all()
    serializer_class = serializers.SequenceRunSerializer

class SampleSheetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SampleSheet.objects.all()
    serializer_class = serializers.SampleSheetSerializer
