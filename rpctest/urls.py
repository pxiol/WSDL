from django.conf.urls import patterns, url
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView
from rpctest.core.views import app, HelloWorldService


urlpatterns = patterns('',
    url(r'^hello_world/','core.views.hello_world_service'),
    
    url(r'^say_hello/', DjangoView.as_view(
        services=[HelloWorldService], tns='spyne.examples.django',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
    
    url(r'^api/', DjangoView.as_view(application=app)),
)
