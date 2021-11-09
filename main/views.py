from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(req):
    return HttpResponse("Hello World!")
def test(req):
    return render(req, "test.html")