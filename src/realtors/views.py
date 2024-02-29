from django.shortcuts import render
from django.views import View
from . import forms


# Create your views here.
class Agents_View(View):
    def get(self, request):
        return render(request, "realtors/agents.html")


class Contact_View(View):
    form = forms.ContactForm()

    def get(self, request):
        return render(request, "realtors/contact.html", {"form": self.form})
