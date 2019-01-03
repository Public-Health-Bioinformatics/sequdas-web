from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from . import models

admin.site.register(models.Sequencer)
admin.site.register(models.MiseqSampleSheet)

@admin.register(models.SequenceRun)
class SequenceRunParentAdmin(PolymorphicParentModelAdmin):
    base_model = models.SequenceRun
    child_models = (models.MiseqSequenceRun, models.MinionSequenceRun)

@admin.register(models.MiseqSequenceRun)
class MiseqSequenceRunAdmin(PolymorphicChildModelAdmin):
    base_model = models.MiseqSequenceRun

@admin.register(models.MinionSequenceRun)
class MiseqSequenceRunAdmin(PolymorphicChildModelAdmin):
    base_model = models.MinionSequenceRun
