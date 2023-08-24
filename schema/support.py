from peewee import SQL, DateField, ForeignKeyField
from .base_model import BaseModel
from .person import CharField, Person

class Support(BaseModel):
    military_number = ForeignKeyField(Person, primary_key=True)
    annexation_date = DateField()
    detachment = CharField()

    def __str__(self):
        return f"{self.military_number}\t{self.annexation_date}\t{self.detachment}\t"
