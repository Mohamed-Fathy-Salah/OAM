from enum import Enum
from peewee import AutoField, DateField, ForeignKeyField
from .base_model import BaseModel
from .person import Person

class Penalty(BaseModel):
    penalty_id = AutoField()
    military_number = ForeignKeyField(Person)
    from_date = DateField()
    to_date = DateField()
    penalty_type = Enum("prison", "detention")

    def __str__(self):
        return f"{self.penalty_id}\t{self.military_number}\t{self.from_date}\t{self.to_date}\t{self.penalty_type}\t"
