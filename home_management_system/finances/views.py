from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Paycheck, Bill
from django.shortcuts import redirect
from .forms import CreateNewBill

def index(request):
    form = CreateNewBill(request.POST)
    paychecks = Paycheck.objects.all()
    bills = Bill.objects.all()
    context = {"bills":bills, "paychecks": paychecks, "form":form}
    return render(request, 'finances/index.html.django', context)


def create_new_bill(request):
    if request.POST:
        print(request.POST)
        form = CreateNewBill(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/finances/')


#
# def deletex(request, id):
#     print(request.POST)
#     return redirect('/finances/')


    # # t.save() # this will update only
def add_bill_to_paycheck(request):
    return redirect('/finances/')





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

# def add(request):
#   template = loader.get_template('add.html')
#   return HttpResponse(template.render({}, request))
#
#  def addrecord(request):
#   first = request.POST['first']
#   last = request.POST['last']
#   member = Members(firstname=first, lastname=last)
#   member.save()
#
# return HttpResponseRedirect(reverse('index'))
#
# def delete(request, id):
#   member = Members.objects.get(id=id)
#   member.delete()
#   return HttpResponseRedirect(reverse('index'))
#
# def update(request, id):
#   mymember = Members.objects.get(id=id)
#   template = loader.get_template('update.html')
#   context = {
#     'mymember': mymember,
#   }
