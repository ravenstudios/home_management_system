from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Chore, Day
from .forms import AddNewChore, CompleteChore
from accounts.models import FamilyMember
from django.utils import timezone



def index(request):
    chores = Chore.objects.all
    add_new_chore = AddNewChore(request.POST)
    completed_chore = CompleteChore(request.POST)
    week = Day.objects.all
    context = {
        "chores" : chores,
        "add_new_chore" : add_new_chore,
        "week" : week,
        "completed_chore" : completed_chore,
    }
    return render(request, 'chores/index.html.django', context)



def add_new_chore(request, day_id):
    post = request.POST

    if post:
        new_chore = AddNewChore(post)
        day = Day.objects.get(id=day_id)

        if new_chore.is_valid():
            chore_name = post.get("chore_name")
            note = post.get("note")
            assigned_to = FamilyMember.objects.get(id=post.get("assigned_to"))
            new_chore.save(commit=False)

            chore = Chore.objects.create(
                chore_name = chore_name,
                note = note,
                assigned_to = assigned_to,
                date_created = timezone.now()
                )

            day.chores.add(chore)

        else:
            print(form.errors.as_data())

    return redirect('/chores/')



def complete_chore(request, chore_id, day_id):
    post = request.POST
    day = Day.objects.get(id=day_id)




    if post:
        chore = Chore.objects.get(id=chore_id)

        note = post.get("note")
        completed = post.get("completed")
        parents_completed = post.get("parents_completed")


        if completed == "true":
            completed = True
            chore.chore_status = "done"
            chore.date_completed = timezone.now()
        else:
            completed = False
            chore.chore_status = "pending"

        if parents_completed == "true":
            parents_completed = True
            chore.chore_status = "parent_approved"
            chore.date_parent_completed = timezone.now()
        else:
            parents_completed = False


        chore.note += "\n" + note
        chore.completed = completed

        if parents_completed:
            chore.parents_completed = parents_completed
            day.chores.remove(chore)


        chore.save()

    return redirect('/chores/')
