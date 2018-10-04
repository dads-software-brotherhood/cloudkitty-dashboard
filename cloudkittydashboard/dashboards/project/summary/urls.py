from django.conf.urls import patterns
from django.conf.urls import url

from cloudkittydashboard.dashboards.project.summary import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
)
