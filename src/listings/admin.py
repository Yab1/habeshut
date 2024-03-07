from django.contrib import admin
from .models import Aminitie, FloorPlan, Photo, Property, Status, Type

# Register your models here.
admin.site.register(Property)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(FloorPlan)
admin.site.register(Photo)
admin.site.register(Aminitie)
