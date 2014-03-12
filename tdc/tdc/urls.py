from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from frontend.views import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^gallery/$', GalleryListView.as_view(), name='gallery_list'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
    {'template_name': 'login.html', 'extra_context': {'next':'/gallery/'}}),
    url(r'^impressum/', TemplateView.as_view(template_name="impressum.html"), name='impressum'),
    url(r'^gallery/(?P<pk>\d+)/$', GalleryDetailView.as_view(), name='gallery_detail'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))