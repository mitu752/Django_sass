from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from utils.email.mail import send_email

def send_email1(request):
    send_email("sakdfjfdj32423532959539952953@qq.com")
    return HttpResponse("success")