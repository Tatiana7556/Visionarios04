from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Create your views here.

def pqr(request):
    return render(request,'PSQR.html')


def contact(request):
    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        subject= request.POST['subject']
        message= request.POST['message']

        template = render_to_string('email_template.html',{
            'name':name,
            'email':email,
            'message':message,
        })

        email= EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['gelmarelectrodomesticos@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request,'Se ha enviado tu PQR.')
        return redirect('pqr')