from rest_framework import viewsets
from django.contrib.auth.models import User
from . import models
from . import serializers

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class SequencerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Sequencer.objects.all()
    serializer_class = serializers.SequencerSerializer

class MiseqSequenceRunViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MiseqSequenceRun.objects.all()
    serializer_class = serializers.MiseqSequenceRunSerializer

class MiseqSampleSheetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MiseqSampleSheet.objects.all()
    serializer_class = serializers.MiseqSampleSheetSerializer

class MiseqSampleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MiseqSample.objects.all()
    serializer_class = serializers.MiseqSampleSerializer
