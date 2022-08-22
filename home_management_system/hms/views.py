from django.shortcuts import render
from django.http import HttpResponse
from .forms import UpdateTask



def index(request):
    context = {
        
    }
    return render(request, 'hms/index.html.django', context)


def update_message(request, message_id):
    print(message_id)
    # name = request.POST.get("name")
    # ammount = request.POST.get("ammount")
    # date = request.POST.get("date")
    # bill = Bill.objects.get(id=bill_id)
    # bill.name = name
    # bill.ammount = ammount
    # bill.due_date = date
    # bill.save()
    # if request.POST:
    #     form = CreateNewBill(request.POST)
    #     if form.is_valid():
    #         form.save()
    return redirect('/hms/')

# Create your views here.
