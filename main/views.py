from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def home(req):
    return render(req, "index.html")

def test(req):
    todo_list = ToDo.objects.all()
    return render(req, "test.html", { "todo_list": todo_list })

def meetings(req):
    tomeet_list = ToMeet.objects.all()
    return render(req, "meetings.html", { "tomeet_list": tomeet_list })

def add_todo(req):
    form = req.POST
    todo = ToDo(text=form["todo-input"])
    todo.save()
    return redirect(test)