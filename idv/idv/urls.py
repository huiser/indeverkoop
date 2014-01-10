from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='frontpage.html'), name='home'),
    url(r'^producten$', TemplateView.as_view(template_name="producten.html"), name="producten"),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
)
