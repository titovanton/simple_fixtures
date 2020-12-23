import os

from django.apps import apps
from django.core.management import call_command
from django.core.management.base import BaseCommand

from ..mixins import BaseMixin


class Command(BaseMixin, BaseCommand):
    def fix_name(self, model):
        return '{}_{}.json'.format(*model.split('.'))

    def handle(self, *args, **options):
        for model in self.fixtures_index:
            if model in self.black_list:
                print('    (!) skipping {}: in the black list'.format(model))
                continue
            output = os.path.join(self.fixtures_folder, self.fix_name(model))
            app_label, model_label = model.split('.')
            model_class = apps.get_app_config(app_label).get_model(model_label)
            using = ''
            params = ['dumpdata', model, ]
            fields_labels = [obj.name for obj in model_class._meta.fields]
            if any([
                model in self.force_natural_fk,
                'content_type' in fields_labels
            ]):
                using = '(using --natural-foreign)'
                params += ['--natural-foreign', ]
            print('    exporting{} {} -> {}'.format(using, model, output))
            call_command(*params, output=output, indent=self.indent)
