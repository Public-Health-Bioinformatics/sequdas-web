from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('sequencers', views.SequencerViewSet)
router.register('sequenceruns', views.MiseqSequenceRunViewSet)
router.register('miseqsamplesheets', views.MiseqSampleSheetViewSet)
router.register('miseqsamples', views.MiseqSampleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
