from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from chores.models import Chore, ChoreLogs
from django.utils.timezone import now, localtime
import datetime

class Command(BaseCommand):
    help = 'Refreshes status for all chores '

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        chores = Chore.objects.all()
        days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
        today = timezone.now().weekday()

        for chore in chores:
            if chore.day_assigned == days[today]:
                if chore.chore_status == "late":
                    chore.chore_status = "failed"
                    # *** Do more here later

                # *** Copies instance of chore to model ChoreLogs by looping through attrs
                chore_logs = ChoreLogs()
                chore_logs.__dict__ = chore.__dict__
                d = datetime.datetime.now()
                chore_logs.chore_name = chore.chore_name + " " + d.strftime("%m-%d-%Y")
                chore_logs.save()

                if chore.repeated_chore:
                    chore.chore_status = "pending"
                    chore.completed = False
                    chore.date_created = datetime.datetime.now()
                    chore.date_completed = datetime.datetime.now()
                    chore.save()
                else:
                    chore.delete()
