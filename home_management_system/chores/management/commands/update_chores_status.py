from django.core.management.base import BaseCommand, CommandError
from chores.models import Chore

class Command(BaseCommand):
    help = 'Refreshes status for all chores '

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        chores = Chore.objects.all()

        for chore in chores:
            chore.chore_status = "pending"
            chore.save()
