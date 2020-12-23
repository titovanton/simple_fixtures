import importlib
import os

from django.apps import apps
from django.conf import settings


class BaseMixin:
    fixtures_index_module = importlib.import_module(settings.FIXTURES_INDEX)
    fixtures_app = settings.FIXTURES_INDEX.split('.')[0]
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

    @property
    def fixtures_index(self):
        return self.fixtures_index_module.fixtures_index

    @property
    def fixtures_folder(self):
        return os.path.join(settings.BASE_DIR, self.fixtures_app, 'fixtures')

    def __init__(self, *args, **options):
        # validation
        assert apps.get_app_config(self.fixtures_app)
        super().__init__(*args, **options)
