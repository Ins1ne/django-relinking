from django.conf.urls import patterns
from django.conf.urls import url

from app import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index_page"),
    url(r'^show/(?P<pk>\d+)/$', views.show, name="display_model"),
    url(r'^hello/', views.CustomView.as_view(), name="text_page"),
)
