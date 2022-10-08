from django.shortcuts import render
from django.http import HttpResponse,request
import pywhatkit

def op(request):
    return render(request,'index.html')

def sendmsg(request):
    number = request.GET['pnone']
    msg = request.GET['msgone']
    ans = pywhatkit.sendwhatmsg_instantly(number,msg)

    return render(request,'success.html',{'result':ans})
