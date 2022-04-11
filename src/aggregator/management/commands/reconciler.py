from django.core.management.base import BaseCommand

from reconciler.reconliator import Reconciliator
from aggregator.repository import MusicRepository


class Command(BaseCommand):
    help = 'Process and reconcile music metadata'

    def add_arguments(self, parser) -> None:
        parser.add_argument('metadata', nargs='+', type=str)
    
    def handle(self, *args, **options):
        csv_file = options['metadata'][0]
        self.stdout.write(f'Processing music entries in {csv_file}')

        music_repository = MusicRepository()
        reconciler = Reconciliator(music_repository)
        reconciler.read_csv(csv_file)

        self.stdout.write(f'Succesfully finished processing {csv_file}')
