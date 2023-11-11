from django.shortcuts import render
from django.http import HttpResponse
#hien thi trang web
# Create your views here.
def home(request):
    return render(request,'app/home.html') #render: hien thi trang web

    