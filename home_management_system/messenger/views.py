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