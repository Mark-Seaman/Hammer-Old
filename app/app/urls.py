from django.contrib import admin
admin.autodiscover()

from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.views.generic import TemplateView

def hello(request):
    return HttpResponse('<h1>Hello, Mark</h1><a href="about">About</a>')

urlpatterns = patterns('',
    url(r'^$', hello),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html")),

    url(r'^admin/', include(admin.site.urls)),
)
