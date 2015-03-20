from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'app.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )

def hello(request):
    return HttpResponse('<h1>Hello-World</h1>'+\
                        '<p>This app has a hard-coded templates</p>')

urlpatterns = patterns('',
    url(r'^$', hello),
)
