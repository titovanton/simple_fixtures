import importlib

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


fixtures_index = importlib.import_module(settings.FIXTURES_INDEX).fixtures_index


class Command(BaseCommand):
    black_list = [
        'auth.group_permissions',
        'auth.permission',
        'auth.user_groups',
        'auth.user_user_permissions',
        'django.admin_log',
        'django.content_type',
        'django.migrations',
        'django.session',
    ]

    def fix_name(self, model):
        return '{}.json'.format(model.replace('.', '_'))

    def handle(self, *args, **options):
        print('\n')
        for model in fixtures_index:
            if model in self.black_list:
                print('    (!) skipping {}: in the black list'.format(model))
                continue
            print('    Loading {} <- {}'.format(model, self.fix_name(model)))
            call_command('loaddata',
                         self.fix_name(model),
                         app=settings.FIXTURES_APP)
