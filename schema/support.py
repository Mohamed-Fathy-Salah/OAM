from peewee import SQL, CompositeKey, DateField, ForeignKeyField, PrimaryKeyField
from .base_model import BaseModel
from .person import CharField, Person

class Support(BaseModel):
    military_number = ForeignKeyField(Person)
    date_of_annexation = DateField()
    detachment = CharField()

    class Meta:
        constants = [SQL('PRIMARY KEY (military_number)')]

    def __str__(self):
        return f"{self.military_number}\t{self.date_of_annexation}\t{self.detachment}\t"
