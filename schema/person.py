from enum import Enum
from peewee import DateField, CharField, FixedCharField, TextField, ValuesList
from .base_model import BaseModel
from .enum_field import EnumField
from .types import state

class Person(BaseModel):
    military_number = FixedCharField(primary_key= True)
    rank = TextField() # todo: make index with name
    name = CharField() 
    residence = CharField()
    brigade = CharField()
    demobilization_date = DateField()
    phone_number = CharField()
    national_id = CharField()
    state = EnumField(choices= state)
    return_date = DateField()

    def __str__(self):
        return f"{self.military_number}\t{self.rank}\t{self.name}\t{self.residence}\t{self.brigade}\t{self.demobilization_date}\t{self.phone_number}\t{self.national_id}\t{self.state}\t{self.return_date}\n"
    # def __str__(self):
        # return f"military_number = {self.military_number}\nrank = {self.rank}\nname = {self.name}\nresidence = {self.residence}\nbrigade = {self.brigade}\ndemobilization date = {self.demobilization_date}\nphone number = {self.phone_number}\nnational id = {self.national_id}\n"
