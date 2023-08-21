from peewee import DateField, ForeignKeyField
from .base_model import BaseModel
from .person import CharField, Person

class Penalty(BaseModel):
    military_number = ForeignKeyField(Person, )
    date_of_annexation = DateField()
    detachment = CharField()

    def __str__(self):
        return f"{self.military_number}\t{self.date_of_annexation}\t{self.detachment}\t"
