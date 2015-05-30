from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crops_and_markets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # administrator
    url(r'^admin/', include(admin.site.urls)),

    # index
    url(r'^$', 'crops_and_markets_app.views.home', name='home'),
    url(r'^index/', 'crops_and_markets_app.views.home', name='home'),
    url(r'^home/', 'crops_and_markets_app.views.home', name='home'),
    
    # crops
    url(r'^crops/', 'crops_and_markets_app.views.crops', name='crops'),
    
    # markets
    url(r'^markets/', 'crops_and_markets_app.views.markets', name='markets')
)
