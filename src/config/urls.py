from os import name
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("faq/", TemplateView.as_view(template_name="pages/faq.html"), name="faq"),
    path("admin/", admin.site.urls),
    path("properties/", include("listings.urls", namespace="listings")),
    path("agents/", include("realtors.urls", namespace="realtors")),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
