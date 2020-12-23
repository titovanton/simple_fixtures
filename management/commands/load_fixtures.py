from django.core.management import call_command
from django.core.management.base import BaseCommand

from ..mixins import BaseMixin


class Command(BaseMixin, BaseCommand):
    def fix_name(self, model):
        return '{}.json'.format(model.replace('.', '_'))

    def handle(self, *args, **options):
        print('\n')
        for model in self.fixtures_index:
            if model in self.black_list:
                print('    (!) skipping {}: in the black list'.format(model))
                continue
            print('    Loading {} <- {}'.format(model, self.fix_name(model)))
            call_command('loaddata', self.fix_name(model), app=self.fixtures_app)
