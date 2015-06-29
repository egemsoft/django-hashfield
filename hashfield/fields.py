from django.db import models
from .utils import hashit


class HashField(models.CharField):
    description = (
        'HashField is related to some other field in a model and stores its hashed value for better indexing performance.')

    def __init__(self, populate_from=None, *args, **kwargs):
        '''
        :param populate_from: name of the field storing the value to be hashed
        '''
        self.populate_from = populate_from
        kwargs['max_length'] = 40
        kwargs['null'] = False
        kwargs.setdefault('db_index', True)
        kwargs.setdefault('editable', False)
        super(HashField, self).__init__(*args, **kwargs)

    def calculate_hash(self, model_instance):
        original_value = []

        if type(self.populate_from) is str:
            original_value.append(getattr(model_instance, self.populate_from))

        else:

            for field_str in self.populate_from:
                original_value.append(str(getattr(model_instance, field_str)))

        setattr(model_instance, self.attname, hashit(original_value))

    def pre_save(self, model_instance, add):
        self.calculate_hash(model_instance)
        return super(HashField, self).pre_save(model_instance, add)


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^hashfield\.fields\.HashField"])
except ImportError:
    pass
