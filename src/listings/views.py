from django.shortcuts import render
from django.views import View
from . import forms


# Create your views here.
class Properties_View(View):
    def get(self, request):
        return render(request, "listings/properties.html")


class Property_Detail_View(View):
    form = forms.AgentForm()

    def get(self, request, id):
        context = {"id": id, "form": self.form}
        return render(request, "listings/property_detail.html", context)
