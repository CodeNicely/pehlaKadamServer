from django.contrib import admin
from .models import *
# Register your models here.
class geo_location_dataAdmin(admin.ModelAdmin):
	list_display=["marker","latitude","longitude"]
admin.site.register(geo_location_data,geo_location_dataAdmin)

