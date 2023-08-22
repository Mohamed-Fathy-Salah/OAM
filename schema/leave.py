from peewee import AutoField, DateField, CharField, ForeignKeyField
from .base_model import BaseModel
from .person import Person

class Leave(BaseModel):
    leave_id = AutoField()
    military_number = ForeignKeyField(Person) #todo: back ref
    from_date = DateField()
    to_date = DateField()
    return_date = DateField()
    travel_form_1 = CharField()
    travel_form_2 = CharField()
    leave_type = CharField()

    def __str__(self):
        return f"{self.leave_id}\t{self.military_number}\t{self.from_date}\t{self.to_date}\t{self.travel_form_1}\t{self.travel_form_2}\t"
