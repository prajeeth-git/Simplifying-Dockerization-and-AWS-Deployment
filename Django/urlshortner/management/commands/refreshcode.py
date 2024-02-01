from django.core.management.base import BaseCommand, CommandError

from urlshortner.models import urlshortner

class Command(BaseCommand):
    help = "Refreshes all urlshortner"

    def add_arguments(self, parser):
        parser.add_argument('--items',type=int)

    def handle(self, *args, **options):
        print(options)
        return urlshortner.objects.refresh_codes(items=options['items'])
