from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class Home_View(View):
    def get(self, request):
        return render(request, "pages/home.html")
