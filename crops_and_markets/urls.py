from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	# administrator
	url(r'^admin/', include(admin.site.urls)),

	# general views
	url(r'^$', 'crops_and_markets_app.views.login', name='login'),
	url(r'^about', 'crops_and_markets_app.views.about', name='about'),
	url(r'^access_denied', 'crops_and_markets_app.views.access_denied', name='access_denied'),
	url(r'^accounts/login', 'crops_and_markets_app.views.access_denied', name='access_denied'),
	url(r'^export_documents', 'crops_and_markets_app.views.export_documents', name='export_documents'),
	url(r'^index', 'crops_and_markets_app.views.home', name='home'),
	url(r'^home', 'crops_and_markets_app.views.home', name='home'),
	url(r'^logout', 'crops_and_markets_app.views.logout', name='logout'),

	# crops
	url(r'^add_crop', 'crops_and_markets_app.views.add_crop', name='add_crop'),
	url(r'^add_plantation', 'crops_and_markets_app.views.add_plantation', name='add_plantation'),
	url(r'^crop_info', 'crops_and_markets_app.views.crop_info', name='crop_info'),
	url(r'^crop_map', 'crops_and_markets_app.views.crop_map', name='crop_map'),
	url(r'^crop_table', 'crops_and_markets_app.views.crop_table', name='crop_table'),
	url(r'^crops$', 'crops_and_markets_app.views.crops', name='crops'),
	url(r'^export_crops_xlsx', 'crops_and_markets_app.views.export_crops_xlsx', name='export_crops_xlsx'),
	url(r'^photo_library', 'crops_and_markets_app.views.photo_library', name='photo_library'),
	url(r'^plantation_info', 'crops_and_markets_app.views.plantation_info', name='plantation_info'),
	url(r'^plantation_table', 'crops_and_markets_app.views.plantation_table', name='plantation_table'),

	# markets
	url(r'^add_market', 'crops_and_markets_app.views.add_market', name='add_market'),
	url(r'^add_sale', 'crops_and_markets_app.views.add_sale', name='add_sale'),
	url(r'^export_markets_xlsx', 'crops_and_markets_app.views.export_markets_xlsx', name='export_markets_xlsx'),
	url(r'^market_company', 'crops_and_markets_app.views.market_company', name='market_company'),
	url(r'^market_info', 'crops_and_markets_app.views.market_info', name='market_info'),
	url(r'^market_map', 'crops_and_markets_app.views.market_map', name='market_map'),
	url(r'^market_table$', 'crops_and_markets_app.views.market_table', name='market_table'),
	url(r'^market_table_potential', 'crops_and_markets_app.views.market_table_potential', name='market_table_potential'),
	url(r'^markets$', 'crops_and_markets_app.views.markets', name='markets'),
	url(r'^sales_detail', 'crops_and_markets_app.views.sales_detail', name='sales_detail'),
	url(r'^sales_history', 'crops_and_markets_app.views.sales_history', name='sales_history'),

	# related
	url(r'^add_related', 'crops_and_markets_app.views.add_related', name='add_related'), 
	url(r'^related$', 'crops_and_markets_app.views.related', name='related'),
	url(r'^related_info', 'crops_and_markets_app.views.related_info', name='related_info'),
	url(r'^related_table', 'crops_and_markets_app.views.related_table', name='related_table')
)


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
