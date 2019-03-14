from django.contrib import admin

from . import models

admin.site.register(models.Sequencer)
admin.site.register(models.MiseqSampleSheet)
admin.site.register(models.MiseqSample)
admin.site.register(models.MiseqSequencingRun)
admin.site.register(models.MiseqReadSummary)
