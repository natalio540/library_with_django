from django.shortcuts import render,redirect
from .models import clientsTable
from libpanel import settings
from django.core.paginator import Paginator
# importamos forms
from .forms import ClientsForm
#para realizar consultar a la base de datos
from django.db.models import Q



# Create your views here.
        

# show clients
def clients_list(request):
    client_list = clientsTable.objects.all()
    queryset = request.GET.get('buscar')
    if queryset:
        client_list = clientsTable.objects.filter(
            Q(name__icontains= queryset) |
            Q(adress__icontains= queryset) |
            Q(email__icontains= queryset) |
            Q(phone__icontains= queryset) 

        ).distinct()
    return render(request,'clientsLoans/clients.html', {'list':client_list})    


# add and update clients
def clients_form(request,id=0):
    if request.method== "GET":
        if id == 0:
            form = ClientsForm()
        else:
           client = clientsTable.objects.get(pk=id)
           form = ClientsForm(instance=client)     
        return render(request,'clientsLoans/addclient.html',{'form':form})            
    else:
        if id == 0:
            form = ClientsForm(request.POST)
        else:
            book = clientsTable.objects.get(pk=id)
            form = ClientsForm(request.POST, instance= book)     
        if form.is_valid():
            form.save()             
        return redirect('/clientsLoans/clients')

# delete clients
def client_delete(request,id):
    client = clientsTable.objects.get(pk=id)
    client.delete()
    return redirect('/clientsLoans/clients')
