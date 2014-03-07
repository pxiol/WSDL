from django.conf.urls import patterns, url
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView
from rpctest.core.views import api, api2


urlpatterns = patterns('',
    #url(r'^hello_world/','core.views.hello_world_service'),
    
    url(r'^say_hello/', DjangoView.as_view(
        services=[api], tns='app_operaciones',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),

    url(r'^say_hello2/', DjangoView.as_view(
        services=[api2], tns='app_operaciones',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
    
   # url(r'^api/', DjangoView.as_view(application=app)),
)