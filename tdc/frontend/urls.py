from django.conf.urls import url, patterns
from frontend.views import *

urlpatterns = patterns('',
    url(r'^/', HomeView.as_view(), name='home'),
    url(r'^design/', DesignListView.as_view(), name='design_list'),
)
