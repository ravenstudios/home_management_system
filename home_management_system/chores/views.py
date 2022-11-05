from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Chore
from .forms import AddNewChore, CompleteChore
from accounts.models import FamilyMember
from django.utils import timezone



def index(request):
    days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
    week = []


    for day in days:
        # week.append({"day" : day, "chores" : []})
        week.append([day, []])

    for chore in Chore.objects.all():
        day = chore.day_assigned
        day_index = days.index(chore.day_assigned)
        week[day_index][1].append(chore)

    add_new_chore = AddNewChore(request.POST)
    completed_chore = CompleteChore(request.POST)
    context = {
        # "chores" : chores,
        "add_new_chore" : add_new_chore,
        "completed_chore" : completed_chore,
        "week": week,
        "users" : ["Jordan"],
    }
    return render(request, 'chores/index.html.django', context)



def add_new_chore(request, day, user):
    post = request.POST
    if post:
        new_chore = AddNewChore(post)


        if new_chore.is_valid():
            chore_name = post.get("chore_name")
            note = post.get("note")
            assigned_to = FamilyMember.objects.get(name=user)
            day_assigned = day
            new_chore.save(commit=False)

            repeated_chore = post.get("repeated_chore")

            if repeated_chore == "true":
                repeated_chore = True
            else:
                repeated_chore = False

            chore = Chore.objects.create(
                chore_name = chore_name,
                note = note,
                assigned_to = assigned_to,
                date_created = timezone.now(),
                repeated_chore = repeated_chore,
                day_assigned = day_assigned
                )



        else:
            print(form.errors.as_data())

    return redirect('/chores/')


def start_chore(request, chore_id):
    post = request.POST
    print(f"post: {chore_id}")
    if True:
        print(f"post: {post}")
        chore = Chore.objects.get(id=chore_id)
        chore.chore_start_time = timezone.now()
        chore.chore_status = "in_progress"
        print(f"chore name: {chore.chore_name}")
        chore.save()
    return redirect('/chores/')



def complete_chore(request, chore_id,  user):
    post = request.POST

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
        chore.save()


        if parents_completed:
            chore.parents_completed = parents_completed

            if not chore.repeated_chore:
                chore.delete()
            else:
                chore.save()




    return redirect('/chores/')
