from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
def callpostmethod(request):
    return HttpResponse('post')


def callgetmethod(request):
    url="http://localhost:8000/API/list"
    head={'contnet-type':'application/json'}
    res=requests.get(url=url,headers=head)
    #print(res.status_code)
    print(res.json())
    return HttpResponse('post')