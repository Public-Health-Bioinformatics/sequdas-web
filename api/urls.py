from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('sequencers', views.SequencerViewSet)
router.register('sequence-runs', views.SequenceRunViewSet)
router.register('sample-sheets', views.MiseqSampleSheetViewSet)

urlpatterns = [
    path('', include(router.urls))
]
