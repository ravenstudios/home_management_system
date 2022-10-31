from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from chores.models import Chore
from django.utils.timezone import now, localtime
import datetime
from django.shortcuts import redirect
from twilio.rest import Client
import text_message
import requests
from django.conf import settings



class Command(BaseCommand):
    help = 'Refreshes status for all chores '

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)
# THIS WILL RUN AT 8:OO PM EVERYDAY WITH CRONTAB TO MARK CHORES LATE




    def handle(self, *args, **options):
        days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
        today = timezone.now().weekday()

        chores = Chore.objects.all()

        late_chore_names = ""
        num_of_late_chores = 0

        for chore in chores:
            if chore.day_assigned == days[today]:
                if not chore.completed:
                    chore.chore_status = "late"
                    chore.save()
                    num_of_late_chores += 1
                    late_chore_names += f"{chore.chore_name}\n"

        if num_of_late_chores > 0:
            phone_numbers = ["2544622979", "2545353255", "2544150271‬"]
            print("late chores")

            message = f"You have {num_of_late_chores} late chores.\n {late_chore_names} Do them now or be beaten.\n But please, have a nice day"

            account_sid = settings.ACCOUNT_SID
            auth_token = settings.AUTH_TOKEN
            client = Client(account_sid, auth_token)

            for pn in phone_numbers:

                client.messages.create(
                                        body = message,
                                        from_= '+18593281744',
                                        to = pn
                                    )

            return "sent"
