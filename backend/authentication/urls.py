from django.conf.urls import url

from . import views

app_name = 'authentication'
urlpatterns = [
    url(r'^login/$', views.login_page, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signup/$', views.sign_up, name='signup')
]