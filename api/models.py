from django.db import models

class Sequencer(models.Model):
    manufacturer = models.CharField(max_length=256, blank=True)
    model_name = models.CharField(max_length=256, blank=True)
    sequencer_id = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.sequencer_id

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
    reverse_complement = models.NullBooleanField()
    adapter = models.CharField(max_length=128, blank=True)
    adapter_read2 = models.CharField(max_length=128, blank=True)
    read1_length = models.IntegerField()
    read2_length = models.IntegerField()
    def __str__(self):
        return (str(self.date) + ": " + self.project_name + "/" + self.experiment_name)

class MiseqSample(models.Model):
    sample_sheet = models.ForeignKey(MiseqSampleSheet, related_name='samples', on_delete=models.CASCADE)
    sample_id = models.CharField(max_length=256, blank=False)
    sample_name = models.CharField(max_length=256, blank=True, null=True)
    sample_plate = models.CharField(max_length=256, blank=True, null=True)
    sample_well = models.CharField(max_length=256, blank=True, null=True)
    index_1_i7_index_id = models.CharField(max_length=16, blank=True, null=True)
    index_1_i7_index_seq = models.CharField(max_length=16, blank=True, null=True)
    index_2_i5_index_id = models.CharField(max_length=16, blank=True, null=True)
    index_2_i5_index_seq = models.CharField(max_length=16, blank=True, null=True)
    sample_project = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    genome_folder = models.CharField(max_length=256, blank=True, null=True)
    manifest = models.CharField(max_length=256, blank=True, null=True)
    contaminants = models.CharField(max_length=256, blank=True, null=True)
    mirna = models.CharField(max_length=256, blank=True, null=True)
    rna = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return (self.sample_id)

class MiseqSequencingRun(models.Model):
    run_id = models.CharField(max_length=64)
    sequencer = models.ForeignKey(Sequencer, on_delete=models.SET_NULL, null=True)
    folder = models.CharField(max_length=256, blank=True)    
    sample_sheet = models.OneToOneField(MiseqSampleSheet, on_delete=models.PROTECT)
    cluster_density = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    clusters_passed_filter_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    reads_total = models.PositiveIntegerField(blank=True)
    reads_passed_filter = models.PositiveIntegerField(blank=True)
    bases_greater_than_q30_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    def __str__(self):
        return self.run_id

class MiseqReadSummary(models.Model):
    sequence_run = models.ForeignKey(MiseqSequencingRun, on_delete=models.CASCADE, related_name='read_summaries')
    READ_TYPE_CHOICES = (
        ('READ_1', 'Read 1'),
        ('INDEX_1', 'Index 1'),
        ('INDEX_2', 'Index 2'),
        ('READ_2', 'Read 2'),
        ('NON_INDEXED', 'Non-indexed'),
    )
    read_type = models.CharField(max_length=32, choices=READ_TYPE_CHOICES, blank=True)
    yield_gigabases = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    projected_yield_gigabases = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    aligned_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    error_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    intensity_c1 = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    bases_greater_than_q30_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return (self.sequence_run.run_id + ": " + self.read_type)
