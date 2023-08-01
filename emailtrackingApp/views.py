from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Email

from django.core.mail import EmailMessage


def compose_email(request):
    """ This function will 
        take the structure of mail and Save it in Database 
    """
    if request.method == 'POST':
        subject = request.POST['subject']
        body = request.POST['body']
        recipients = request.POST['recipients']
       
        email = Email(subject=subject, body=body, recipients=recipients)
        email.save()

    return redirect("all_user_email")


def image(request, id):
    """
        Once the user recieves the mail,
        to track we will be send link that will redirect in backend, where have we can get an update.
    """

    user = Email.objects.get(id = id)
    user.opened_at =  datetime.now()
    user.save()

    return render(request, "image.html")


def all_user_email(request):
    """ This will return the user model table data
        you can view and track the data of an email.
    """
    all_mail = Email.objects.all()
    return render(request, "compose_email.html", {"all_mail":all_mail})


def multimail(request):
    """Here will be sending the mail to the receipts
    we can either send single mail, 
    or you can send multiple mail"""

    if request.method=="POST":
        selected_email = request.POST["selected-emails"]
        email_list = selected_email.split(',')
        for i in email_list:
            email_data=Email.objects.get(id = int(i))
            subject = email_data.subject
            body_mail = email_data.body
            data = "http://127.0.0.1:8000/image/"+ str(i)

            wishing = "\n\n Thanks Regards,\n Anam Khan."

            body = body_mail + '\n\n\n' + "Its Good to have Greetings!!!.\nPlease Click on the Link and see +_+  " + data + wishing

            recipients =[email_data.recipients,]

            email_data.sent_at = datetime.now()
            email_data.save()

            email = EmailMessage(subject, body,to = recipients)
            email.send()

    return redirect("all_user_email")

