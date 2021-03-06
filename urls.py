from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from apps.views import HomePage


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePage.as_view(), name="home-page"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^edit/', include('person.urls')),
    url(r'^requests/', include('db_requests.urls')),
)

#If this local dev-server, using static.serve
if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns("django.views",
         (r'^static/(?P<path>.*)$', 'static.serve', {'document_root': settings.STATIC_ROOT,
            'show_indexes': True,}),
    )
