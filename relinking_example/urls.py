from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from app import urls as app_urls
from django_relinking import urls as relinking_urls

urlpatterns = patterns(
    '',
    url('', include(app_urls)),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^admin/relinking/', include(relinking_urls)),
)
