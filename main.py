from datetime import date
from peewee import DateField, SqliteDatabase, Model, CharField, FixedCharField, TextField

db = SqliteDatabase('OAM.db')

class BaseModel(Model):
    class Meta:
        database = db

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

db.connect()
db.create_tables([Person])

# mofasa = Person.create(military_number= '1234123131223', name= 'محمد فتحي صلاح', rank= 'جندي', residence= 'القاهره', brigade= 'ت.أ', demobilization_date= date(year= 2024, month= 3, day= 1), phone_number= '01111234567', national_id= '123412345698034')

print(Person.select()[:])

