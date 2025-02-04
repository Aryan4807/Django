from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("welcome to my routing bro")

def contact(request):
    return HttpResponse("my contact are huge")
def about(request):
    return HttpResponse("i will be kickass ")