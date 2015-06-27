from django.db import models
from .fields import HashField
from .utils import hashit


class HashManager(models.Manager):
    _hash_field_name = None

    @property
    def hash_field_name(self):
        if self._hash_field_name is None:

            for field in self.model._meta.fields:
                if isinstance(field, HashField):
                    self._hash_field_name = field.name

        return self._hash_field_name

    def hash_keys(self, **kwargs):
        return list(self.filter(**kwargs).values_list(self.hash_field_name, flat=True))

    def update_or_create(self, keys, defaults=None, return_object=False, **kwargs):
        """
        Looks up an object with the given kwargs, updating one with defaults
        if it exists, otherwise creates a new one.
        Returns a tuple (object, created), where created is a boolean
        specifying whether an object was created.
        """
        defaults = defaults or {}
        hashed_params = []

        for field in self.model._meta.fields:
            if isinstance(field, HashField):
                populate_from = getattr(field, 'populate_from', [])
                for p in populate_from:
                    if p in kwargs:
                        hashed_params.append(str(kwargs.get(p, None)))
            from django.db.models import DateTimeField

        hash_key = hashit(''.join(hashed_params))

        if hash_key in keys:
            for field in self.model._meta.fields:
                if isinstance(field, DateTimeField):
                    auto_now = getattr(field, 'auto_now', None)
                    if auto_now:
                        import datetime

                        defaults[field.name] = datetime.datetime.now()
            obj = self.filter(**{self.hash_field_name: hash_key}).update(**defaults)
            created = False
        else:
            obj = self.model(**dict(kwargs.items() + defaults.items())).save()
            created = True

        if return_object:
            obj = self.get(**{self.hash_field_name: hash_key})

        return obj, created
