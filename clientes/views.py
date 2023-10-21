from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from clientes.forms import ClienteForm
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all()
    context = {'clientes' : clientes}
    return render(request, 'clientes/index.html', context)

def form_cliente(request):
    if request.method == 'GET':
        form = ClienteForm()
        context = {
            'form' : form
        }
        return render(request, 'clientes/formclientes.html', context)
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClienteForm()
            return redirect('index')                  
        else:
            context = {
            'form' : form
            }
            return render(request, 'clientes/index.html', context)
        
def detalhe_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        raise Http404('O cliente não existe')
    return render(request, 'clientes/detalhe_cliente.html', {'cliente':cliente})


def delete_cliente(request, id):
    try:
        cliente = Cliente.objects.filter(id=id)
        cliente.delete()
    except Cliente.DoesNotExist:
        raise Http404('Cliente não existe')
    return redirect('index')

def update_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'cliente': cliente, 'form': form}
    return render(request, 'clientes/update_cliente.html', context)