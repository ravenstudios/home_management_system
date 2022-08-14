from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Item, List
from django.shortcuts import redirect
# from .forms import CreateNewBill, CreateNewPaycheck, UpdateMoneyInBank, UpdateBill, PayBill
from django.db.models import Sum


def index(request):
    # create_new_bill = CreateNewBill(request.POST)
    # create_new_paycheck = CreateNewPaycheck(request.POST)
    # update_money_in_bank = UpdateMoneyInBank(request.POST)
    # update_bill = UpdateBill(request.POST)
    # # pay_bill = PayBill(request.POST)
    # paychecks = Paycheck.objects.all()
    # bills = Bill.objects.all()
    # # bills_total = bills.aggregate(Sum('ammount'))
    # context = {
    #     "bills":bills,
    #     "paychecks": paychecks,
    #     "create_new_bill":create_new_bill,
    #     "create_new_paycheck":create_new_paycheck,
    #     "add_bill_to_paycheck":add_bill_to_paycheck,
    #     "update_money_in_bank": update_money_in_bank,
    #     "update_bill": update_bill,
    #     "pay_bill": pay_bill,
    #      }
    #
    # context["pay_bill"] = PayBill(request.POST)
    # for paycheck in paychecks:
    #     update_values(paycheck)
    context={}
    return render(request, 'shopping_list/index.html.django', context)
