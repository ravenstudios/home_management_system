from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Paycheck, Bill

def index(request):


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


def create_new_bill(request):

    post = request.POST
    name = post.get("name")
    ammount = post.get("ammount")
    due_date = post.get("due_date")
    obj, created = Bill.objects.update_or_create(name=name, ammount=ammount, due_date = due_date)

    return  HttpResponse("created new bill")
