from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        "variablq":"dsasda"
    }
    return render(request,"index.html",context)
    # return HttpResponse("welcome to my routing bro")

def contact(request):
    return HttpResponse("my contact are huge")
def about(request):
    return HttpResponse("About us ")
def services(request):
    return HttpResponse("services Contact us ")