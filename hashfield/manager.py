from django.db import models
from .fields import HashField
from .utils import hashit


class HashManager(models.Manager):
    hash_field_name = 'hash_key'

    def hash_keys(self, **kwargs):
        qs = super(HashManager, self).get_query_set()
        return list(qs.filter(**kwargs).values_list(self.get_hash_field_name(), flat=True))

    def get_hash_field_name(self):
        qs = self.get_query_set()
        for field in qs.model._meta.fields:
            if isinstance(field, HashField):
                self.hash_field_name = field.name
                return field.name

    def update_or_create(self, keys, defaults=None, **kwargs):
        """
        Looks up an object with the given kwargs, updating one with defaults
        if it exists, otherwise creates a new one.
        Returns a tuple (object, created), where created is a boolean
        specifying whether an object was created.
        """
        self.get_hash_field_name()
        qs = self.get_query_set()

        defaults = defaults or {}
        # lookup, params = self._extract_model_params(defaults, **kwargs)
        hashed_params = []

        for field in qs.model._meta.fields:
            if isinstance(field, HashField):
                populate_from = getattr(field, 'populate_from', [])
                for p in populate_from:
                    if p in kwargs:
                        hashed_params.append(str(kwargs.get(p, None)))

        hash_key = hashit(''.join(hashed_params))

        if hash_key in keys:
            obj = qs.filter(**{self.hash_field_name: hash_key}).update(**defaults)
            created = False
        else:
            obj = qs.model(**dict(kwargs.items() + defaults.items())).save()
            created = True

        return obj, created