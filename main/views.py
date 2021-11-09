from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def home(req):
    return render(req, "index.html")

def test(req):
    todo_list = ToDo.objects.all()
    return render(req, "test.html", { "todo_list": todo_list })

def add_todo(req):
    form = req.POST
    todo = ToDo(text=form["todo-input"])
    todo.save()
    return redirect(test)

def delete_todo(req, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(req, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not(todo.is_favorite)
    todo.save()
    return redirect(test)

def toggle_todo(req, id):
    todo = ToDo.objects.get(id=id)
    todo.is_done = not(todo.is_done)
    todo.save()
    return redirect(test)

def meetings(req):
    tomeet_list = ToMeet.objects.all()
    return render(req, "meetings.html", { "tomeet_list": tomeet_list })

def add_meeting(req):
    form = req.POST
    meeting = ToMeet(
        persone=form["meeting-persone"],
        phone_number=form["meeting-phonenumber"],
        date_meeting=form["meeting-date"]
    )
    if ("meeting-done" in form):
        meeting.is_done = True
    if ("meeting-favorite" in form):
        meeting.is_favorite = True
    meeting.save()
    return redirect(meetings)

def delete_meeting(req, id):
    meeting = ToMeet.objects.get(id=id)
    meeting.delete()
    return redirect(meetings)

def mark_meeting(req, id):
    meeting = ToMeet.objects.get(id=id)
    meeting.is_favorite = not(meeting.is_favorite)
    meeting.save()
    return redirect(meetings)

def habits(req):
    habits_list = Habit.objects.all()
    return render(req, "habits.html", { "habits_list": habits_list })

def add_habit(req):
    form = req.POST
    habit = Habit(
        habit_description=form["habit-description"]
    )
    if ("habit-is-done-today" in form):
        habit.is_done_today = True
    if ("habit-is-important" in form):
        habit.is_important = True
    habit.save()
    return redirect(habits)
