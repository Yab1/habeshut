from email.mime import image
from email.policy import default
from enum import unique
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Type(models.Model):
    class Property_Type(models.TextChoices):
        APARTMENT = "Apartment", _("Apartment")
        CONDOMINIUM = "Condominium", _("Condominium")
        G_1 = "G+1 House", _("G+1 House")
        G_2 = "G+2 House", _("G+2 House")
        MANSION = "Mansion", _("Mansion")
        VILLA = "Villa", _("Villa")

    name = models.CharField(
        max_length=15, choices=Property_Type.choices, default=Property_Type.APARTMENT
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property Type"
        verbose_name_plural = "Property Types"


class Status(models.Model):
    class Property_Status(models.TextChoices):
        RENT = "Rent", _("Rent")
        SELL = "Sell", _("Sell")

    name = models.CharField(
        max_length=10, choices=Property_Status.choices, default=Property_Status.SELL
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property Status"
        verbose_name_plural = "Property Status"


class Property(models.Model):
    name = models.CharField(max_length=100)
    property_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    propery_status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    description = models.TextField(default="", max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
