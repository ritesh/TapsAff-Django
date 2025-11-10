from django.urls import re_path

from . import views

app_name = 'www'
urlpatterns = [
    re_path(r'^$', views.Index.as_view(), name='index'),
    re_path(r'^api/(?P<location>[\w\-\ \+ \']+)/$', views.Api.as_view(), name='api'),
    re_path(r'^(?P<location>[\w\-\ \+ \']+)/$', views.Index.as_view(), name='index'),
    re_path(r'^map/clothing$', views.Map.as_view(), {'show': 'clothing'}, name='clothing'),
    re_path(r'^map/weather$', views.Map.as_view(), {'show': 'weather'}, name='weather'),
]
