from __future__ import unicode_literals

from django.db import models

# Create your models here.
class geo_location_data(models.Model):
	marker=models.CharField(max_length=50,blank=False,null=False)
	latitude=models.FloatField(blank=False,null=False)
	longitude=models.FloatField(blank=False,null=False)

