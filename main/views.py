from django.shortcuts import render, HttpResponse
from .models import ToDo

# Create your views here.
def home(req):
    return render(req, "index.html")

def test(req):
    todo_list = ToDo.objects.all()
    return render(req, "test.html", { "todo_list": todo_list })