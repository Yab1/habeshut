from django.urls import path
from . import views

app_name = "listings"
urlpatterns = [
    path("all/", views.Properties_View.as_view(), name="properties"),
    path("<int:id>/", views.Property_Detail_View.as_view(), name="property_detail"),
]
