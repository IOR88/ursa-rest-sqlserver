from __future__ import unicode_literals

from django.core.management import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app')

    def handle(self, *args, **options):
        inspected_app = options['app']
        my_app = apps.get_app_config(inspected_app)
        print('from django.conf.urls import url, include')
        print('from rest_framework import routers')
        print('from %s import views' % inspected_app)
        print('')
        print('router = routers.DefaultRouter()')
        for my_model_name, my_model_class in my_app.models.items():
            print("router.register(r'%s', views.%sViewSet)" % (str(my_model_name).title(), str(my_model_name).title()))
        print('')
        print('urlpatterns = [')
        print("    url(r'^', include(router.urls)),")
        print("    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),")
        print(']')
