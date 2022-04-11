from lib2to3.pytree import Base
from django.core.management.base import BaseCommand, CommandError

from reconciler.reconliator import Reconciliator
from aggregator.repository import MusicRepository


class Command(BaseCommand):
    help = 'Process and reconcile music metadata'

    def add_arguments(self, parser) -> None:
        parser.add_argument('metadata', nargs='+', type=str)
    
    def handle(self, *args, **options):
        self.stdout.write(f'Processing music entries in {options["metadata"]}')

        music_repository = MusicRepository()
        reconciler = Reconciliator(music_repository)
        reconciler.read_csv(options['metadata'])

        self.stdout.write(f'Succesfully finished processing {options["metadata"]}')
