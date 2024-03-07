from django.db import models
from django.utils.translation import gettext_lazy as _
from realtors.models import Agent


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
        max_length=15,
        choices=Property_Type.choices,
        default=Property_Type.APARTMENT,
        unique=True,
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
        max_length=10,
        choices=Property_Status.choices,
        default=Property_Status.SELL,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property Status"
        verbose_name_plural = "Property Status"


class Aminitie(models.Model):
    class Aminities(models.TextChoices):
        BALCONY = "Balcony", _("Balcony")
        CHILDRENS_PLAYGROUND = "Children's Playground", _("Children's Playground")
        DECK = "Deck", _("Deck")
        ELEVATOR = "Elevator", _("Elevator")
        FITNESS_CENTER = "Fitness Center", _("Fitness Center")
        GARDEN = "Garden", _("Garden")
        HOT_TUB = "Hot Tub", _("Hot Tub")
        MODERN_INTERIOR_DESIGN = "Modern Interior Design", _("Modern Interior Design")
        OUTDOOR_KITCHEN = "Outdoor Kitchen", _("Outdoor Kitchen")
        PARKING_SPACE = "Parking Space", _("Parking Space")
        ROOFTOP_TERRACE = "Rooftop Terrace", _("Rooftop Terrace")
        SOLAR_PANELS = "Solar Panels", _("Solar Panels")
        SPA = "Spa", _("Spa")
        SPORTS_COURT = "Sports Court", _("Sports Court")
        SURVEILLANCE_SYSTEM = "Surveillance System", _("Surveillance System")
        SWIMMING_POOL = "Swimming Pool", _("Swimming Pool")

    name = models.CharField(
        max_length=50, choices=Aminities.choices, default=Aminities.BALCONY, unique=True
    )


class FloorPlan(models.Model):
    image = models.ImageField(upload_to="floor_plans/")


class Photo(models.Model):
    image = models.ImageField(upload_to="photos/")


class Property(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    property_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    propery_status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    # location =
    area = models.FloatField(
        help_text="Enter the area of the property in square meters."
    )
    beds = models.IntegerField(
        help_text="Enter the number of bedrooms in the property."
    )
    bath = models.IntegerField(
        help_text="Enter the number of bathrooms in the property."
    )
    photos = models.ManyToManyField(Photo)
    floor_plans = models.ManyToManyField(FloorPlan)
    agent = models.ManyToManyField(Agent)
    aminitie = models.ManyToManyField(Aminitie)
    description = models.TextField(default="", max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
