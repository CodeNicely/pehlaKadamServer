from django.contrib import admin
from django.db import models
# Register your models here.
class geo_location_dataAdmin(admin.ModelAdmin):
	list_display=('marker','latitude','longitude')

