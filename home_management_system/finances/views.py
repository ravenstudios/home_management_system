from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Paycheck, Bill
from django.shortcuts import redirect
from .forms import CreateNewBill

def index(request):
    create_new_bill = CreateNewBill(request.POST)
    paychecks = Paycheck.objects.all()
    bills = Bill.objects.all()
    context = {"bills":bills, "paychecks": paychecks, "create_new_bill":create_new_bill, "add_bill_to_paycheck":add_bill_to_paycheck}
    return render(request, 'finances/index.html.django', context)


def create_new_bill(request):
    if request.POST:
        print(request.POST)
        form = CreateNewBill(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/finances/')


def add_bill_to_paycheck(request, name, date):
    # print(f"bill: {bill}")

    if request.POST:
        bill_id = request.POST.getlist('bill', None)
        bill = Bill.objects.get(id=bill_id[0])
        print(f"bill {bill}")
        paycheck = Paycheck.objects.get(name=name, date=date)
        paycheck.bills.add(bill)
        


    return redirect('/finances/')
    # return HttpResponse(request)



def delete_bill(request, name, date):
    paycheck = Paycheck.objects.get(name=name, date=date)
    paycheck.delete()
    #   return HttpResponseRedirect(reverse('index'))
    return redirect('/finances/')



def delete_paycheck(request, name, date):
    print(name, date)
    paycheck = Paycheck.objects.get(name=name, date=date)
    paycheck.delete()
    #   return HttpResponseRedirect(reverse('index'))
    return redirect('/finances/')
