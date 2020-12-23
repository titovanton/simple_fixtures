import importlib
import os

from django.apps import apps
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


fixtures_index = importlib.import_module(settings.FIXTURES_INDEX).fixtures_index


class Command(BaseCommand):
    indent = 2
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
    force_natural_fk = [
        'auth.user',
    ]

    def fix_name(self, model):
        return '{}_{}.json'.format(*model.split('.'))

    def handle(self, *args, **options):
        for model in fixtures_index:
            if model in self.black_list:
                print('    (!) skipping {}: in the black list'.format(model))
                continue
            output = os.path.join(settings.BASE_DIR,
                                  settings.FIXTURES_APP,
                                  'fixtures',
                                  self.fix_name(model))
            app_label, model_label = model.split('.')
            model_class = apps.get_app_config(app_label).get_model(model_label)
            using = ''
            params = ['dumpdata', model, ]
            fields_labels = [obj.name for obj in model_class._meta.fields]
            if (
                model in self.force_natural_fk or
                'content_type' in fields_labels
            ):
                using = '(using --natural-foreign)'
                params += ['--natural-foreign', ]
            print('    exporting{} {} -> {}'.format(using, model, output))
            call_command(*params, output=output, indent=self.indent)
