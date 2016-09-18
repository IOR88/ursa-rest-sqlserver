from __future__ import unicode_literals

from django.core.management import BaseCommand

from django.apps import apps


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app')

    def handle(self, *args, **options):
        inspected_app = options['app']
        my_app = apps.get_app_config(inspected_app)
        # start_time = time.time()
        # self.stdout.write("Staring serialization...")
        print('from rest_framework.serializers import HyperlinkedModelSerializer')
        print('from %s import models' % inspected_app)
        for my_model_name, my_model_class in my_app.models.items():
            my_model_fields = [f.name for f in my_model_class._meta.get_fields()]
            # my_model_fields = (f.name for f in my_model_class._meta.get_fields()) # as generator
            print('')
            print('')
            print('class %sSerializer(HyperlinkedModelSerializer):' % str(my_model_name).title())
            print('')
            print('    class Meta:')
            print('        model = models.%s' % str(my_model_name).title())
            print("        fields = '__all__'")
            print('        # fields =%s' % str(tuple(my_model_fields)))

            # yield ''
            # yield 'class %sSerializer(HyperlinkedModelSerializer):' % my_model_name
            # yield ''
            # yield '    class Meta:'
            # yield '        model = %s' % my_model_name
            # yield "        fields = '__all__'"
            # yield '        # fields =%s' % str(tuple(my_model_fields))
        # self.stdout.write("All models serialized now in %s seconds." % (time.time() - start_time))


