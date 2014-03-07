from spyne.model.primitive import Integer
from spyne.protocol.soap import Soap11
from spyne.service import ServiceBase
from spyne.decorator import rpc


class Operaciones(ServiceBase):
    @rpc(Integer, Integer, Integer)
    def suma(ctx, num1, num2, resul):
        resul = num1 + num2
        return resul

    @rpc(Integer, Integer, Integer)     
    def rest(ctx, num1, num2, resul):
        resul = num1 - num2
        return resul 

    @rpc(Integer, Integer, Integer)     
    def mult(ctx, num1, num2, resul):
        resul = num1 * num2
        return resul        

    @rpc(Integer, Integer, Integer)     
    def divi(ctx, num1, num2, resul):
        resul = num1 / num2
        return resul 
