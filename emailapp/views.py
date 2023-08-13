from django.shortcuts import render

from django.contrib.auth.models import User
from datetime import datetime
from .utils import sen_email_with_html_body

# Create your views here.


def register_view(request, *args, **kwargs):
    """
    creer un pour tester l'envoie de message
    """
    context = {}
    if request.method == 'POST':
        email = request.POST.get("email")

        subjet = 'Test du mail'
        template = 'email.html'
        context = {
            'date': datetime.today(),
            'email': email

        }

        receivers = [email]

        has_send = sen_email_with_html_body(
            subjet=subjet, receivers=receivers, template=template, context=context)

        if has_send:
            context = {"msg": "message envoyer avec success"}
        else:
            context = {"msg": "message echouer"}

    return render(request, 'index.html', context)
