from django.shortcuts import render
from django.http import HttpResponse
# import datetime
from .models import Message
from django.shortcuts import redirect
from .forms import UpdateMessage, CreateNewMessage
from datetime import datetime
from accounts.models import FamilyMember
# from django.db.models import Sum
# from django.contrib.auth.decorators import login_required
# from accounts.models import FamilyMember


def update_message(request, message_id):
    print(message_id)
    message = Message.objects.get(id=message_id)
    message.task_options = request.POST.get("task_options")
    message.time_updated = datetime.now()
    message.comments = request.POST.get("comments")
    message.save()
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
    return redirect('/messenger/')


def add_new_message(request):
    print(request.POST)
    if request.POST:
        form = CreateNewMessage(request.POST)

        if form.is_valid():
            # form.msg_author = FamilyMember.objects.get(name=request.POST.get("msg_author"))
            form.save()
        else:
            print(form.errors.as_data())
    return redirect('/messenger/')


def delete_message(request, message_id):
    Message.objects.get(id=message_id).delete()
    return redirect('/messenger/')

def index(request):
    family_members = FamilyMember.objects.all()
    update_message = UpdateMessage(request.POST)
    add_new_message = CreateNewMessage(request.POST)

    context={
            "messages": Message.objects.all(),
            "update_message": update_message,
            "add_new_message": add_new_message,
            "family_members": family_members,
            "add_new_message": add_new_message,
        }
    return render(request, 'messenger/index.html.django', context)



# def create_new_item(request):
#     if request.POST:
#         form = CreateNewItem(request.POST)
#         if form.is_valid():
#             form.save()
#     return redirect('/shopping_list/')
#
#
#
#
# def delete_item(request, list_id, item_id):
#     list = List.objects.get(id=list_id)
#     item = Item.objects.get(id=item_id)
#     list.items.remove(item)
#     return redirect('/shopping_list/')
#
#
# def edit_item(request, item_id):
#     name = request.POST.get("name")
#     note = request.POST.get("note")
#     date = request.POST.get("date")
#     # list = List.objects.get(id=list_id)
#     item = Item.objects.get(id=item_id)
#     item.name = name
#     item.note = note
#     item.date = date
#     item.save()
#     # list.items.remove(item)
#     return redirect('/shopping_list/')
#
# def edit_list(request, list_id):
#     name = request.POST.get("name")
#     note = request.POST.get("note")
#     date = request.POST.get("date")
#     list = List.objects.get(id=list_id)
#     list.name = name
#     list.note = note
#     list.date = date
#     list.save()
#     # list.items.remove(item)
#     return redirect('/shopping_list/')
#
#
#
#
# def delete_list(request, list_id):
#     list = List.objects.get(id=list_id)
#     for item in list.items.all():
#         item.delete()
#     list.delete()
#     return redirect('/shopping_list/')
#
#
#
# def create_new_list(request):
#     print(request)
#     if request.POST:
#         form = CreateNewList(request.POST)
#         if form.is_valid():
#             form.save()
#     return redirect('/shopping_list/')
#
#
#
# def add_item_to_list(request, list_id):
#     print(request.POST.get("name"))
#     list = List.objects.get(id=list_id)
#     name = request.POST.get("name")
#     note = request.POST.get("note")
#     date = request.POST.get("date")
#     requested_from_name = request.POST.get("family_members")
#     print(f"fm: {requested_from_name}")
#     requested_from = FamilyMember.objects.get(name=requested_from_name)
#
#     item = Item.objects.create(name=name, note=note, requested_from=requested_from)
#     list.items.add(item)
#
#
#
#
#     return redirect('/shopping_list/')
