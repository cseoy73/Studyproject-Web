# from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<h1>장고 공부를 재미있게 하자</h1>")
# Create your views here.
