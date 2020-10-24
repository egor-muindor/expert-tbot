from orator import Model
from orator.orm import belongs_to


class Attribute(Model):
    __table__ = 'attributes'
    __incrementing__ = True
    __timestamps__ = False
    __fillable__ = ['value', 'type_id']
    __casts__ = {
        'id': 'int'
    }

    @belongs_to('type_id', 'id', 'attribute_types')
    def objects(self):
        from . import AttributeType

        return AttributeType
