from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

#from profiles.forms import LoginForm
from profiles.views import ProfielView, ProfielAanpassenView, RegistrerenView
#from django.views.generic import DetailView



from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='frontpage.html'), name='home'),
    url(r'^producten$', TemplateView.as_view(template_name="producten.html"), name='producten'),
    url(r'^woning/', include('woning.urls')),
    #url(r'^inloggen$', 'profiles.views.inloggen', name='inloggen'),
    url(r'^inloggen$', 'django.contrib.auth.views.login',
        {
            'template_name': 'inloggen.html',
        },
        name='inloggen'
    ),
    url(r'^uitloggen$', 'django.contrib.auth.views.logout',
        {
            'next_page': 'home',
        },
        name='uitloggen'
    ),
    #url(r'^uitloggen$', 'profiles.views.uitloggen', name='uitloggen'),
    #url(r'^profiel$', 'profiles.views.profiel', name='profiel'),
    url(r'^profiel$', login_required(ProfielView.as_view()), name='profiel'),
    url(r'^profiel/aanpassen$', login_required(ProfielAanpassenView.as_view()),
        {
            'success_url': 'profiel',
        },
        name='profielaanpassen'
    ),
    url(r'^registreren$', RegistrerenView.as_view(),
        {
            'success_url': 'profiel',
        },
        name='registreren'
    ),
    #url(r'^profiel$', DetailView.as_view(model=), name='profiel'),
    url(r'^admin/', include(admin.site.urls)),
)
