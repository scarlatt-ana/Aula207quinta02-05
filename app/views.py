from django.shortcuts import render
from app.forms import PedidoForm


# Create your views here.

def Fazer_Pedido(request):
    msg= ''
    formulario = PedidoForm(request.POST or None)

    if formulario.is_valid ():
        formulario.save()
        formulario = PedidoForm()
        msg =  'Pedido realizado com sucesso'


    contexto = {
        'form' : formulario,
        'msg': msg
    }



    return render (request, 'index.html', contexto)