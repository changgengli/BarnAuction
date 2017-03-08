from django.conf.urls import include, url

from django.contrib import admin
from auction import views as auction_views

admin.autodiscover()

urlpatterns = [
    # url(r'^$', 'pyweb.views.home', name='home'),
    url(r'^auction/', auction_views.index, name='index'),
    url(r'^auction/bill/', auction_views.bill, name='bill'),
    url(r'^auction/winners/', auction_views.winners, name='winners' ),
    url(r'^admin/', include(admin.site.urls)),
]
