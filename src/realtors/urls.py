from django.urls import path
from . import views

app_name = "realtors"
urlpatterns = [
    path("all/", views.Agents_View.as_view(), name="agents"),
    path("contact/", views.Contact_View.as_view(), name="contact"),
]
