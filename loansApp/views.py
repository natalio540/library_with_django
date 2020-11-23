from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from libpanel import settings
from .models import loansTable
from .forms import LoansForm,LoansFormUpdate
from django.core.paginator import Paginator



# Create your views here.

# show loans
def loans_list(request):
    qs = loansTable.objects.all()
    paginator = Paginator(qs,5)
    page_number = request.GET.get('page',1)
    number_of_loans = len(qs)

    try:
        page_obj = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        raise Http404(f'Invalid page {page_number}. That page contains no results')
    context = {'list':qs, 'object_list': page_obj,'page_obj': page_obj,'num':number_of_loans}

    return render(request, 'loansApp/loans.html',context)

# add loan
def loan_add(request):
    mensaje=''
    if request.method == 'POST':
        form= LoansForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/loansApp/loans')
        else:
            mensaje='the book is not available'     
    else:
        form= LoansForm()            
    return render (request,'loansApp/addloan.html',{'form':form,'mensaje':mensaje})   

# delete loan
def loan_delete(request,id):
    loan=loansTable.objects.get(pk=id)
    loan.delete()
    return redirect ('/loansApp/loans')


# update loan
def loan_update(request,id):
    loan = loansTable.objects.get(id=id)
    if request.method == 'GET':
        form = LoansFormUpdate(instance=loan)
        contexto = {
            'form':form
        }
    else:           
        loan = loansTable.objects.get(pk=id)
        form= LoansFormUpdate(request.POST,instance=loan)
        if form.is_valid():
            form.save()
        return redirect('/loansApp/loans')

    return render (request,'loansApp/addloan.html',contexto)   
 