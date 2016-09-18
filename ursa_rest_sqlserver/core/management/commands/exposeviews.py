from __future__ import unicode_literals

from django.core.management import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app')

    def handle(self, *args, **options):
        inspected_app = options['app']
        my_app = apps.get_app_config(inspected_app)
        print('from rest_framework.viewsets import ModelViewSet')
        print('from %s import models' % inspected_app)
        print('from %s import serializers' % inspected_app)
        print('from %s import filters' % inspected_app)
        for my_model_name, my_model_class in my_app.models.items():
            print('')
            print('')
            print('class %sViewSet(ModelViewSet):' % str(my_model_name).title())
            print('')
            print('    queryset = models.%s.objects.all()' % str(my_model_name).title())
            print('    serializer_class = serializers.%sSerializer' % str(my_model_name).title())
            print('    filter_class = filters.%sFilterSet' % str(my_model_name).title())
            print("    # filter_fields = ('type_filed_name_here',)")
            print("    # search_fields = ('type_filed_name_here',)")
