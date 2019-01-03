from django.db import models
from polymorphic.models import PolymorphicModel    
    
class MiseqSampleSheet(models.Model):
    path = models.CharField(max_length=256, blank=True)
    iem_file_version = models.CharField(max_length=8, blank=True)
    investigator_name = models.CharField(max_length=64, blank=True)
    project_name = models.CharField(max_length=64, blank=True)
    experiment_name = models.CharField(max_length=64, blank=True)
    date = models.DateField()
    workflow = models.CharField(max_length=64, blank=True)
    assay = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=64, blank=True)
    chemistry = models.CharField(max_length=64, blank=True)
    application = models.CharField(max_length=64, blank=True)
    read1_length = models.IntegerField()
    read2_length = models.IntegerField()
    reverse_complement = models.NullBooleanField()
    adapter = models.CharField(max_length=128, blank=True)
    adapter_read2 = models.CharField(max_length=128, blank=True)
    def __str__(self):
        return (str(self.date) + ": " + self.investigator_name + "/" + self.project_name)

class Sequencer(models.Model):
    manufacturer = models.CharField(max_length=256, blank=True)
    model_name = models.CharField(max_length=256, blank=True)
    sequencer_id = models.CharField(max_length=256, blank=True)

class SequenceRun(PolymorphicModel):
    run_id = models.CharField(max_length=64)
    sequencer = models.ForeignKey(Sequencer, on_delete=models.SET_NULL, null=True)

class MiseqSequenceRun(SequenceRun):
    sample_sheet = models.ForeignKey(
        MiseqSampleSheet,
        on_delete=models.SET_NULL,
        null=True
    )
    folder = models.CharField(max_length=256, blank=True)
    cluster_density = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    clusters_passed_filter_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    reads_total = models.PositiveIntegerField(blank=True)
    reads_passed_filter = models.PositiveIntegerField(blank=True)
    bases_greater_than_q30_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    def __str__(self):
        return self.run_id

class MinionSequenceRun(SequenceRun):
    reads_total = models.PositiveIntegerField(blank=True)
    
class Sample(PolymorphicModel):
    sample_id = models.CharField(max_length=64)
    sample_name = models.CharField(max_length=64, blank=True)
    def __str__(self):
        return (self.sequence_run.run_id + ": " + self.sample_id + "/" + self.sample_name)

class MiseqSample(Sample):
    sample_sheet = models.ForeignKey(
        MiseqSampleSheet,
        on_delete = models.CASCADE
    )
    index_1_i7_seq = models.CharField(max_length=16, blank=True)
    index_2_i5_seq = models.CharField(max_length=16, blank=True)
    def __str__(self):
        return (str(self.sample_sheet) + "/" + self.sample_id)

class MinionSample(Sample):
    barcode_seq = models.CharField(max_length=16, blank=True)
    
class IridaSample(models.Model):
    irida_project = models.CharField(max_length=64, blank=False)
    sample  = models.ForeignKey(
        Sample,
        on_delete = models.CASCADE
    )
    
class MiseqReadSummary(models.Model):
    sequence_run = models.ForeignKey(SequenceRun, on_delete=models.CASCADE, related_name='read_summaries')
    READ_TYPE_CHOICES = (
        ('READ_1', 'Read 1'),
        ('INDEX_1', 'Index 1'),
        ('INDEX_2', 'Index 2'),
        ('READ_2', 'Read 2'),
    )
    read_type = models.CharField(max_length=32, choices=READ_TYPE_CHOICES, blank=True)
    yield_gigabases = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    error_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    bases_greater_than_q30_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    def __str__(self):
        return (self.sequence_run.run_id + ": " + self.read_type)

