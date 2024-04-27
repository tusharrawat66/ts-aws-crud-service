from mongoengine import (Document, StringField, FloatField)



class Equipment(Document):
    name = StringField(required=True)
    description = StringField()
    price = FloatField(required=True)
    tax = FloatField()

    meta = {
        'collection': 'equipment'  # Specify the collection name here
    }