from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from chores.models import Chore
from django.utils.timezone import now, localtime
import datetime

class Command(BaseCommand):
    help = 'Refreshes status for all chores '

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        chores = Chore.objects.all()

        for chore in chores:
            if chore.repeated_chore:
                chore.chore_status = "pending"
                chore.date_created = datetime.datetime.now()
                chore.date_completed = datetime.datetime.now()
                chore.date_parent_completed = datetime.datetime.now()
                chore.save()
