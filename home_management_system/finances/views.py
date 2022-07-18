from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Paycheck, Bill

def index(request):

    obj, created = Paycheck.objects.update_or_create(name="y1oyo", date="7/18/2022", ammount=1123.123)

    paychecks_to_add = []
    paychecks = Paycheck.objects.all()
    bills = Bill.objects.all()

    for paycheck in paychecks:
        paychecks_to_add = []
        for bill in bills:
            if bill != "":
                bill_due_date = int(bill.due_date)
                paycheck_date = int(paycheck.date.split("/")[1])

        #         if bill_due_date <= paycheck_date:
        #             paychecks_to_add.append(bill)
        #
        #
        #
        # for pta in paychecks_to_add:
        #     pta.save()
        #     paycheck.bills.add(pta)










    context = {"bills":bills, "paychecks": paychecks}
    return render(request, 'finances/index.html.django', context)
