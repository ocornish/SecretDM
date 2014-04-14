from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'secret.views.home', name='home'),
    url(r'^message/$', 'secret.views.message', name='message'),
   	url(r'^message/(\d+)$', 'secret.views.messages', name='messages'),
   	url(r'^login/$', 'django.contrib.auth.views.login', name="my_login"),

    # Examples:
    # url(r'^$', 'dm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
