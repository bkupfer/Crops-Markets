from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# administrator
	url(r'^admin/', include(admin.site.urls)),

	# general views
	url(r'^$', 'crops_and_markets_app.views.login', name='login'),
	url(r'^about', 'crops_and_markets_app.views.about', name='about'),
	url(r'^access_denied', 'crops_and_markets_app.views.access_denied', name='access_denied'),
	url(r'^accounts/login', 'crops_and_markets_app.views.access_denied', name='access_denied'),
	url(r'^index', 'crops_and_markets_app.views.home', name='home'),
	url(r'^home', 'crops_and_markets_app.views.home', name='home'),

	# crops
	url(r'^add_crop', 'crops_and_markets_app.views.add_crop', name='add_crop'),
	url(r'^add_owner', 'crops_and_markets_app.views.add_owner', name='add_owner'),
	url(r'^crops', 'crops_and_markets_app.views.crops', name='crops'),
	url(r'^crop_map', 'crops_and_markets_app.views.crop_map', name='crop_map'),
	url(r'^crop_info', 'crops_and_markets_app.views.crop_info', name='crop_info'),
	url(r'^crop_table', 'crops_and_markets_app.views.crop_table', name='crop_table'),
	url(r'^paddock_detail', 'crops_and_markets_app.views.paddock_detail', name='paddock_detail'),

	# markets
	url(r'^add_market', 'crops_and_markets_app.views.add_market', name='add_market'),
	url(r'^add_sale', 'crops_and_markets_app.views.add_sale', name='add_sale'),
	url(r'^markets', 'crops_and_markets_app.views.markets', name='markets'),
	url(r'^market_info', 'crops_and_markets_app.views.market_info', name='market_info'),
	url(r'^market_map', 'crops_and_markets_app.views.market_map', name='market_map'),
	url(r'^market_table$', 'crops_and_markets_app.views.market_table', name='market_table'),
	url(r'^market_table_potential', 'crops_and_markets_app.views.market_table_potential', name='market_table_potential')
)
