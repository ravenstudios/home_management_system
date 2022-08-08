from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Paycheck, Bill
from django.shortcuts import redirect
from .forms import CreateNewBill, CreateNewPaycheck, UpdateMoneyInBank, UpdateBill, PayBill
from django.db.models import Sum


def index(request):
    create_new_bill = CreateNewBill(request.POST)
    create_new_paycheck = CreateNewPaycheck(request.POST)
    update_money_in_bank = UpdateMoneyInBank(request.POST)
    update_bill = UpdateBill(request.POST)
    # pay_bill = PayBill(request.POST)
    paychecks = Paycheck.objects.all()
    bills = Bill.objects.all()
    # bills_total = bills.aggregate(Sum('ammount'))
    context = {
        "bills":bills,
        "paychecks": paychecks,
        "create_new_bill":create_new_bill,
        "create_new_paycheck":create_new_paycheck,
        "add_bill_to_paycheck":add_bill_to_paycheck,
        "update_money_in_bank": update_money_in_bank,
        "update_bill": update_bill,
        "pay_bill": pay_bill,
         }

    context["pay_bill"] = PayBill(request.POST)
    for paycheck in paychecks:
        update_values(paycheck)

    return render(request, 'finances/index.html.django', context)


def pay_bill(request, name, date, bill, paid):
    print(f"paid {paid}")

    paycheck = Paycheck.objects.get(name=name, date=date)
    bill = paycheck.bills.get(name=bill)

    if paid == "0":
        print("paid")
        bill.paid = False
    if paid == "1":
        print("not paid")
        bill.paid = True
    bill.save()
    paycheck.save()
        # for bill in paycheck.bills.all():
            # print(bill.paid)
    return redirect('/finances/')



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
        bill_name = request.POST.getlist('bill', None)
        bill = Bill.objects.get(name=bill_name[0])
        paycheck = Paycheck.objects.get(name=name, date=date)
        paycheck.bills.add(bill)

        update_values(paycheck)
    return redirect('/finances/')



def delete_bill_from_paycheck(request, name, date, bill):
    paycheck = Paycheck.objects.get(name=name, date=date)
    bill = Bill.objects.get(name=bill)
    paycheck.bills.remove(bill)

    update_values(paycheck)
    # paycheck.save(update_fields=['balance'])
    return redirect('/finances/')



def delete_paycheck(request, name, date):
    paycheck = Paycheck.objects.get(name=name, date=date)
    paycheck.delete()
    return redirect('/finances/')


def delete_bill(request, name):
    bill = Bill.objects.get(name=name)
    bill.delete()
    return redirect('/finances/')



def update_money_in_bank(request, name, date):
    paycheck = Paycheck.objects.get(name=name, date=date)
    money_in_bank_ammount = request.POST.get("paycheck.ammount_in_bank")
    paycheck.save(update_fields=['ammount_in_bank'])
    update_values(paycheck)
    return redirect('/finances/')


def update_values(paycheck):
    bills_total = 0
    for bill in paycheck.bills.all():
        if not bill.paid:
            bills_total += bill.ammount

    paycheck.bills_total = bills_total
    paycheck.balance = paycheck.ammount - paycheck.bills_total
    paycheck.save(update_fields=['bills_total', 'balance'])
    return bills_total
