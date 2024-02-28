from django.shortcuts import render
from django.views import View


# Create your views here.
class Agents_View(View):
    def get(self, request):
        return render(request, "realtors/agents.html")


class Contact_View(View):

    def get(self, request):
        return render(request, "realtors/contact.html")
