from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from chores.models import Chore
from django.utils.timezone import now, localtime
import datetime

class Command(BaseCommand):
    help = 'Refreshes status for all chores '

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)
# THIS WILL RUN AT 8:OO PM EVERYDAY WITH CRONTAB TO MARK CHORES LATE



    def handle(self, *args, **options):
        days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
        today = timezone.now().weekday()
        
        chores = Chore.objects.all()

        for chore in chores:
            if chore.day_assigned == days[today]:
                if not chore.completed:
                    chore.chore_status = "late"

                    chore.save()
