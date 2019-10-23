from django.db import models

# Create your models here.
class Report(models.Model):

    class Meta:
        app_label = 'base'

    name = models.CharField(max_length=32)
    total_value = models.IntegerField()
    disk_usage = models.FloatField()
    latency = models.FloatField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.created)