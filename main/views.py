from django.shortcuts import render, HttpResponse

# Create your views here.
def home(req):
    return render(req, "index.html")
def test(req):
    return render(req, "test.html")