from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        "variable":"dsasda"
    }
    return render(request,"index.html",context)
    # return HttpResponse("welcome to my routing bro")

def contact(request):
    return render(request,"contact.html")
    # return HttpResponse("my contact are huge")
def about(request):
   return render(request,"about.html")
def services(request):
   return render(request,"services.html")