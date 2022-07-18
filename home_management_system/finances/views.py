from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    datetime_now = datetime.datetime.now()

    month = datetime_now.strftime("%m")

    paychecks = [
        {"person": "Krystle", "date": "7/1/2022", "ammount": "1100.00", "bills":[]},
        {"person": "Rob", "date": "7/7/2022", "ammount": "100.00", "bills":[]},
        {"person": "Krystle", "date": "7/15/2022", "ammount": "1100.00", "bills":[]},
        {"person": "Rob", "date": "7/21/2022", "ammount": "1000.00", "bills":[]},
        {"person": "Krystle", "date": "7/31/2022", "ammount": "1100.00", "bills":[]},
    ]

    bills = [
        {"bill": "Mortage", "ammount":712.00, "due_date": 31},
        {"bill": "Phone", "ammount":300.00, "due_date": 1},
        {"bill": "Car", "ammount":300.00, "due_date": 13},
        {"bill": "Bike", "ammount":145.00, "due_date": 3},
    ]


    for paycheck in paychecks:
        next_paycheck_index = paychecks.index(paycheck)
        for bill in bills:
            if bill != "":
                bill_due_date = int(bill["due_date"])
                paycheck_date = int(paycheck["date"].split("/")[1])


                next_paycheck_date = int(paychecks[next_paycheck_index + 1]["date"].split("/")[1])
                print(next_paycheck_date)

                # need to get date of next paycheck and see if bill date is in between the 2 dates
                if bill_due_date <= next_paycheck_date:
                    # print("true")
                    paycheck["bills"].append(bill)
                    bills[bills.index(bill)] = ""




        # print(bill_date)
        # x = datetime.datetime(2020, 5, 17)




    context = {"bills":bills, "paychecks": paychecks}
    return render(request, 'finances/index.html.django', context)
