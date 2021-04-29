from django.core.management import BaseCommand
from django_logic.display import display_process

from store.process import LockerProcess


class Command(BaseCommand):

    help = 'Generate graph.'

    def handle(self, *args, **kwargs):
        display_process(LockerProcess, state='open', skip_main_process=True)
