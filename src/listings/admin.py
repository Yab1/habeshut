from django.contrib import admin
from .models import Property, Status, Type

# Register your models here.
admin.site.register(Property)
admin.site.register(Type)
admin.site.register(Status)
