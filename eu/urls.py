from django.conf.urls import patterns, include, url
# from django.contrib import admin

from home import views
# from pages import views


# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^admin/', include(admin.site.urls)),

    # Test URLs to allow you to see these pages while DEBUG is True
    url(r'^error/404/$', views.Error404.as_view(), name='404'),
    url(r'^error/500/$', views.Error500.as_view(), name='500'),

)
