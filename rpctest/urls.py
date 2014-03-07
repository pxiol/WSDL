from django.conf.urls import patterns, url
from spyne.server.django import DjangoView
from rpctest.core.views import Operaciones
from spyne.protocol.soap import Soap11


urlpatterns = patterns('',
    
    url(r'^operaciones/', DjangoView.as_view(
        services=[Operaciones], tns='Operaciones',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),

      
)