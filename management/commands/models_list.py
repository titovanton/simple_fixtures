from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from ..mixins import BaseMixin


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('\n')
        for ct in ContentType.objects.all().order_by('app_label', 'model'):
            label = f'{ct.app_label}.{ct.model}'
            if label not in BaseMixin.black_list:
                print(f'\'{label}\',')
        print('\n')
