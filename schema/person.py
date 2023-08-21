from peewee import DateField, CharField, FixedCharField, TextField
from .base_model import BaseModel

class Person(BaseModel):
    military_number = FixedCharField(primary_key= True)
    rank = TextField() 
    name = CharField()
    residence = CharField()
    brigade = CharField()
    demobilization_date = DateField()
    phone_number = CharField()
    national_id = CharField()

    def __str__(self):
        return f"{self.military_number}\t{self.rank}\t{self.name}\t{self.residence}\t{self.brigade}\t{self.demobilization_date}\t{self.phone_number}\t{self.national_id}\t"
    # def __str__(self):
        # return f"military_number = {self.military_number}\nrank = {self.rank}\nname = {self.name}\nresidence = {self.residence}\nbrigade = {self.brigade}\ndemobilization date = {self.demobilization_date}\nphone number = {self.phone_number}\nnational id = {self.national_id}\n"
