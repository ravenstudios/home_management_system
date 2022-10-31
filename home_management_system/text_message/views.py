from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings




def send_message(to, message):
    account_sid = settings.ACCOUNT_SID
    auth_token = settings.AUTH_TOKEN
    client = Client(account_sid, auth_token)

    client.messages.create(
                            body = message,
                            from_= '+18593281744',
                            to = to
                        )

    return "sent"


def index(request, to, message):
    send_message(to, message)
    context = {}
    return render(request, 'messenger/index.html.django', context)
