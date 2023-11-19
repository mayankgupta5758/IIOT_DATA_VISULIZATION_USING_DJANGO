from django.shortcuts import render, HttpResponse
# from django.http import JsonResponse
import datetime
# import mysql.connector




# Create your views here.
def index(request):
    context = {"variable":"HELLO SUMIT YOU ARE GREAT BELEVE IN YOURSELF"}
    return render(request, 'index.html')
    # return HttpResponse("WELCOME TO IOT DATA VISULIZATION USING DJANGO")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is CSED About Page")



def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("Faculty coordinator")


def lol(request):
    return render(request, 'lol.html')