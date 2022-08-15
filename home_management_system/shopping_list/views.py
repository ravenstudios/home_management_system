from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Item, List
from django.shortcuts import redirect
from .forms import CreateNewItem, CreateNewList
from django.db.models import Sum
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    create_new_item = CreateNewItem(request.POST)
    create_new_list = CreateNewList(request.POST)
    items = Item.objects.all()
    lists = List.objects.all()

    context={
        "create_new_item": create_new_item,
        "create_new_list": create_new_list,
        "items": items,
        "lists": lists,
        }
    return render(request, 'shopping_list/index.html.django', context)

def create_new_item(request):
    if request.POST:
        form = CreateNewItem(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/shopping_list/')




def delete_item(request, list_id, item_id):
    list = List.objects.get(id=list_id)
    item = Item.objects.get(id=item_id)
    list.items.remove(item)
    return redirect('/shopping_list/')


def edit_item(request, item_id):
    name = request.POST.get("name")
    note = request.POST.get("note")
    date = request.POST.get("date")
    # list = List.objects.get(id=list_id)
    item = Item.objects.get(id=item_id)
    item.name = name
    item.note = note
    item.date = date
    item.save()
    # list.items.remove(item)
    return redirect('/shopping_list/')

def edit_list(request, list_id):
    name = request.POST.get("name")
    note = request.POST.get("note")
    date = request.POST.get("date")
    list = List.objects.get(id=list_id)
    list.name = name
    list.note = note
    list.date = date
    list.save()
    # list.items.remove(item)
    return redirect('/shopping_list/')




def delete_list(request, list_id):
    list = List.objects.get(id=list_id)
    for item in list.items.all():
        item.delete()
    list.delete()
    return redirect('/shopping_list/')



def create_new_list(request):
    print(request)
    if request.POST:
        form = CreateNewList(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/shopping_list/')



def add_item_to_list(request, list_id):
    print(request.POST.get("name"))
    list = List.objects.get(id=list_id)
    name = request.POST.get("name")
    note = request.POST.get("note")
    date = request.POST.get("date")
    item = Item.objects.create(name=name, note=note)
    list.items.add(item)




    return redirect('/shopping_list/')
