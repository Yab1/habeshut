from django.shortcuts import render
from django.views import View


# Create your views here.
class Properties_View(View):
    def get(self, request):
        return render(request, "listings/properties.html")


class Property_Detail_View(View):
    def get(self, request, id):
        return render(request, "listings/property_detail.html", {"id": id})
