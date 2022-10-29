from django.shortcuts import render
from twilio.rest import Client
import environ





def send_message(to, message):
    env = environ.Env()
    environ.Env.read_env()
    account_sid = env('ACCOUNT_SID')
    auth_token = env('AUTH_TOKEN')
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
