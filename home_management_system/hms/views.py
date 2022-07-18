from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = {"name": "Rob",
                "age": 39,
                "sex": "Male"}
    return render(request, 'hms/index.html.django', context)


def view2(request):
    return HttpResponse("so gimme da views")

# Create your views here.
