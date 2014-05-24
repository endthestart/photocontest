from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'photocontest.views.contest_home', name='contest_home'),
    url(r'^submit/$', 'photocontest.views.submit', name='submit'),
    url(r'^event/$', 'photocontest.views.event_view', name='event'),
    url(r'^profile/$', 'photocontest.views.profile_view', name='profile'),
    url(r'^upload/$', 'photocontest.views.jfu_upload', name='jfu_upload'),
    url(r'^gallery/$', 'photocontest.views.gallery', name='gallery'),
    url(r'^about/$', 'photocontest.views.about', name='about'),
    url(r'^contact/$', 'photocontest.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
