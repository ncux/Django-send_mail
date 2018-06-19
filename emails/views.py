from django.shortcuts import render
from django.core.mail import send_mail


def send(request):
    template = 'emails/send.html'
    subject = ''
    body = ''
    sender = ''
    recepient = ['']
    fail_silently= False
    send_mail(subject, body, sender, recepient, fail_silently)
    return render(request, template)