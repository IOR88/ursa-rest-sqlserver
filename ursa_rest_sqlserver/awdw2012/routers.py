class AppRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'awdw2012':
            return 'apidb'
        return None
