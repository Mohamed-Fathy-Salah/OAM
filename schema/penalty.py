from peewee import AutoField, DateField, ForeignKeyField
from .base_model import BaseModel
from .person import CharField, Person

class Penalty(BaseModel):
    penalty_id = AutoField()
    military_number = ForeignKeyField(Person)
    from_date = DateField()
    to_date = DateField()
    penalty_type = CharField()

    def __str__(self):
        return f"{self.penalty_id}\t{self.military_number}\t{self.from_date}\t{self.to_date}\t{self.penalty_type}\t"
