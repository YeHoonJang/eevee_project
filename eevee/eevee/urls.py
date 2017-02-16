from django.conf.urls import url
from django.contrib import admin

from rental_gachon.template import views as ev_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ev_views.index, name='index'),
    url(r'^login$', ev_views.login, name='login'),
    url(r'^check_login', ev_views.check_login, name='check_login'),
    url(r'^logout$', ev_views.logout, name='logout'),
    url(r'^logout_process', ev_views.logout_process, name='logout_process'),
    url(r'^user_registration_process', ev_views.user_registration_process, name='user_registration_process'),
]
