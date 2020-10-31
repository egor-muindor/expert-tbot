from orator import Model
from orator.orm import belongs_to_many


class Object(Model):
    __table__ = 'objects'
    __incrementing__ = False
    __timestamps__ = False
    __primary_key__ = 'appid'
    __fillable__ = ['appid', 'name']
    __casts__ = {}

    @belongs_to_many('object_attribute', 'appid', 'attribute_id')
    def attributes(self):
        from . import Attribute

        return Attribute

