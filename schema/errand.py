from peewee import AutoField, DateField, CharField, ForeignKeyField, TextField
from .base_model import BaseModel
from .person import Person

class errand(BaseModel):
    errand_id = AutoField()
    military_number = ForeignKeyField(Person) #todo: back ref
    from_date = DateField()
    to_date = DateField()
    travel_form_1 = CharField()
    travel_form_2 = CharField()
    place = CharField()
    reason = TextField()

    def __str__(self):
        return f"{self.errand_id}\t{self.military_number}\t{self.from_date}\t{self.to_date}\t{self.travel_form_1}\t{self.travel_form_2}\t{self.place}\t{self.reason}"
    # def __str__(self):
        # return f"military_number = {self.military_number}\nrank = {self.rank}\nname = {self.name}\nresidence = {self.residence}\nbrigade = {self.brigade}\ndemobilization date = {self.demobilization_date}\nphone number = {self.phone_number}\nnational id = {self.national_id}\n"
