from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from refer_exp import exp

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'refer_exp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/users/create$', exp.create_user),
    url(r'^api/v1/buyers/all$', exp.all_buyers),
    url(r'^api/v1/sellers/all$', exp.all_sellers),
    url(r'^api/v1/transaction/create$', exp.create_transaction),
    #url(r'^api/v1/transaction/all$', exp.view_all_transactions),
    url(r'^api/v1/company/create$', exp.create_company),
    #url(r'^api/v1/job-application/create$', exp.create_JobApplication),
    #url(r'^api/v1/job-application/view/(\d+)$', exp.view_company_JobApplications),
    url(r'^api/v1/users/(\d+)$', exp.lookup_user),
    url(r'^api/v1/auth/login$', exp.log_in),
    url(r'^api/v1/auth/logout$', exp.log_out),
    #url(r'^api/v1/auth/verify$', exp.check_auth),
    #url(r'^api/v1/auth/delete_old_auth$', exp.delete_old_auth),
    url(r'^api/v1/note/create$', exp.create_note),
		url(r'^api/v1/note/search$', exp.search_note),
		url(r'^api/v1/company/search$', exp.search_company),

)

urlpatterns += staticfiles_urlpatterns()
