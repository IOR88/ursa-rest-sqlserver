from __future__ import unicode_literals

from django.core.management import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app')

    def handle(self, *args, **options):
        inspected_app = options['app']
        my_app = apps.get_app_config(inspected_app)
        print('from rest_framework.filters import FilterSet')
        print('from %s import models' % inspected_app)
        for my_model_name, my_model_class in my_app.models.items():
            my_model_fields = [f.name for f in my_model_class._meta.get_fields()]
            print('')
            print('')
            print('class %sFilterSet(FilterSet):' % str(my_model_name).title())
            print('')
            print('    class Meta:')
            print('        model = models.%s' % str(my_model_name).title())
            print('        fields =%s' % str(list(my_model_fields)))
