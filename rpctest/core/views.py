from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt

from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.server.django import DjangoApplication
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc
from spyne.util.django import DjangoComplexModel

from rpctest.core.models import FieldContainer


class Container(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = FieldContainer
        django_exclude = ['excluded_field']


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in xrange(times):
            yield 'Hello, %s' % name


class ContainerService(ServiceBase):
    @rpc(Integer, _returns=Container)
    def get_container(ctx, pk):
        try:
            return FieldContainer.objects.get(pk=pk)
        except FieldContainer.DoesNotExist:
            raise ResourceNotFoundError('Container')

    @rpc(Container, _returns=Container)
    def create_container(ctx, container):
        try:
            return FieldContainer.objects.create(**container.as_dict())
        except IntegrityError:
            raise ResourceAlreadyExistsError('Container')

app = Application([HelloWorldService, ContainerService],
    'spyne.examples.django',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

hello_world_service = csrf_exempt(DjangoApplication(app))
