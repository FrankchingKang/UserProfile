from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'sign_in/$', views.sign_in, name='sign_in'),
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'sign_out/$', views.sign_out, name='sign_out'),
    url(r'detail/$', views.profile_detail, name='profile_detail'),
    url(r'edit/$', views.profile_edit, name='profile_edit'),
]
