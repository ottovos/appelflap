from django.shortcuts import render
from django.http import HttpResponse

def home(request, customer_id):
    return HttpResponse("The sur_name of the customer is %s." % customer_id)

def about(request):
    return HttpResponse("<h1>About< /h1>")


