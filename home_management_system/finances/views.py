from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Paycheck, Bill
from django.shortcuts import redirect
from .forms import CreateNewBill, CreateNewPaycheck, UpdateMoneyInBank
from django.db.models import Sum


def index(request):
    create_new_bill = CreateNewBill(request.POST)
    create_new_paycheck = CreateNewPaycheck(request.POST)
    update_money_in_bank = UpdateMoneyInBank(request.POST)
    paychecks = Paycheck.objects.all()
    bills = Bill.objects.all()
    bills_total = bills.aggregate(Sum('ammount'))
    context = {
        "bills":bills,
        "paychecks": paychecks,
        "create_new_bill":create_new_bill,
        "create_new_paycheck":create_new_paycheck,
        "add_bill_to_paycheck":add_bill_to_paycheck,
        "bills_total": bills_total,
        "update_money_in_bank": update_money_in_bank,
         }
    return render(request, 'finances/index.html.django', context)



def create_new_bill(request):
    if request.POST:
        form = CreateNewBill(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/finances/')



def create_new_paycheck(request):
    if request.POST:
        form = CreateNewPaycheck(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/finances/')



def add_bill_to_paycheck(request, name, date):
    if request.POST:
        bill_id = request.POST.getlist('bill', None)
        bill = Bill.objects.get(id=bill_id[0])
        paycheck = Paycheck.objects.get(name=name, date=date)
        paycheck.bills.add(bill)
    return redirect('/finances/')



def delete_bill(request, name, date, bill):
    paycheck = Paycheck.objects.get(name=name, date=date)
    bill = Bill.objects.get(id=bill)
    paycheck.bills.remove(bill)
    return redirect('/finances/')



def delete_paycheck(request, name, date):
    paycheck = Paycheck.objects.get(name=name, date=date)
    paycheck.delete()
    return redirect('/finances/')



def update_money_in_bank(request, name, date):
    paycheck = Paycheck.objects.get(name=name, date=date)
    money_in_bank_ammount = request.POST.get("ammount")
    # print(request.POST)
    paycheck.ammount_in_bank = money_in_bank_ammount
    paycheck.save()
    print(f"payckeck: {paycheck}")
    return redirect('/finances/')
