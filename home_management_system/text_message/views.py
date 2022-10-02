from django.shortcuts import render
from twilio.rest import Client





def send_message(to, message):
    account_sid = 'ACd99a2e85a75181fc14af87e02e1aee05'
    auth_token = 'cda44800ad55b5545e3f956981fb0c8b'
    client = Client(account_sid, auth_token)

    client.messages.create(
                            body = message,
                            from_= '+18593281744',
                            to = to
                        )

    return "sent"


def index(request, to, message):
    print(f"to{to}")

    send_message(to, message)
    context = {}
    return render(request, 'finances/index.html.django', context)
