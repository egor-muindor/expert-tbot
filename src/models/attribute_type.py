from orator import Model


class AttributeType(Model):
    __table__ = 'attributes'
    __incrementing__ = True
    __timestamps__ = False
    __fillable__ = ['type', 'is_parameter']
    __casts__ = {
        'id': 'int'
    }