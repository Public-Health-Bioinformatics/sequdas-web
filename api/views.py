from rest_framework import viewsets
from django.contrib.auth.models import User
from . import models
from . import serializers
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['read']
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class SequencerViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['read']
    queryset = models.Sequencer.objects.all()
    serializer_class = serializers.SequencerSerializer

class MiseqSequenceRunViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['read']
    queryset = models.MiseqSequenceRun.objects.all()
    serializer_class = serializers.MiseqSequenceRunSerializer

class MiseqSampleSheetViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['read']
    queryset = models.MiseqSampleSheet.objects.all()
    serializer_class = serializers.MiseqSampleSheetSerializer

class MiseqSampleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['read']
    queryset = models.MiseqSample.objects.all()
    serializer_class = serializers.MiseqSampleSerializer
