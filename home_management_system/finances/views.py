from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Paycheck, Bill
from django.shortcuts import redirect
from .forms import CreateNewBill, CreateNewPaycheck, UpdateMoneyInBank, UpdateBill, PayBill
from django.db.models import Sum
from django.contrib.auth.decorators import login_required



@login_required
# @user_passes_test(not_in_student_group, login_url='/advising/denied/')
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


def pay_bill(request, paycheck_id, bill_id, paid):
    print(request.get_full_path())

    paycheck = Paycheck.objects.get(id=paycheck_id)
    bill = paycheck.bills.get(id=bill_id)

    if paid == "False":
        print("paid")
        bill.paid = False
    if paid == "True":
        print("not paid")
        bill.paid = True
    bill.save()
    paycheck.save()
        # for bill in paycheck.bills.all():
            # print(bill.paid)
    return redirect('/finances/')

def update_bill(request, bill_id):
    print(bill_id)
    name = request.POST.get("name")
    ammount = request.POST.get("ammount")
    date = request.POST.get("date")
    bill = Bill.objects.get(id=bill_id)
    bill.name = name
    bill.ammount = ammount
    bill.due_date = date
    bill.save()
    # if request.POST:
    #     form = CreateNewBill(request.POST)
    #     if form.is_valid():
    #         form.save()
    return redirect('/finances/')



def edit_paycheck(request, paycheck_id):
    print(request.POST.get("name"))
    name = request.POST.get("name")
    ammount = request.POST.get("ammount")
    date = request.POST.get("date")
    paycheck = Paycheck.objects.get(id=paycheck_id)
    paycheck.name = name
    paycheck.ammount = ammount
    paycheck.date = date
    paycheck.save()
    if request.POST:
        form = CreateNewBill(request.POST)
        if form.is_valid():
            form.save()
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



def add_bill_to_paycheck(request, paycheck_id, bill_id):
    print(request.get_full_path())
    # if request.POST:

    paycheck = Paycheck.objects.get(id=paycheck_id)
    bill = Bill.objects.get(id=bill_id)
    print(f"bill: {bill.paid}")
    # bill.save()
    paycheck.bills.add(bill)
    print(paycheck)
    update_values(paycheck)

    return redirect('/finances/')



def delete_bill_from_paycheck(request, paycheck_id, bill_id):
    paycheck = Paycheck.objects.get(id=paycheck_id)
    bill = Bill.objects.get(id=bill_id)
    paycheck.bills.remove(bill)

    update_values(paycheck)
    # paycheck.save(update_fields=['balance'])
    return redirect('/finances/')



def delete_paycheck(request, paycheck_id):
    paycheck = Paycheck.objects.get(id=paycheck_id)
    paycheck.delete()
    return redirect('/finances/')


def delete_bill(request, bill_id):
    bill = Bill.objects.get(id=bill_id)
    bill.delete()
    return redirect('/finances/')



def update_money_in_bank(request, paycheck_id):
    paycheck = Paycheck.objects.get(id=paycheck_id)
    paycheck.ammount_in_bank = request.POST.get("ammount_in_bank")
    paycheck.save(update_fields=['ammount_in_bank'])
    update_values(paycheck)
    return redirect('/finances/')


def update_values(paycheck):
    bills_total = 0
    bills = paycheck.bills.all()
    if paycheck.bills.all():
        for bill in paycheck.bills.all():
            if not bill.paid:
                bills_total += bill.ammount

    paycheck.bills_total = bills_total
    paycheck.balance = float(paycheck.ammount_in_bank) - float(paycheck.bills_total)
    paycheck.save(update_fields=['bills_total', 'balance'])
    return bills_total
