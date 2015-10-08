from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from refer_exp import exp

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'refer_exp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/buyers/all/', exp.all_buyers),
    url(r'^api/v1/sellers/all', exp.all_sellers)
)
