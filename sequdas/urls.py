from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sequdas import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('sequence-runs', views.SequenceRunViewSet)
router.register('sample-sheets', views.SampleSheetViewSet)

urlpatterns = [
    path('', include(router.urls))
]
