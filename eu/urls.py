from django.conf.urls import patterns, include, url
# from django.contrib import admin

from home import views
# from pages import views


# admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', include('public_site.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^admin/', include(admin.site.urls)),
)
