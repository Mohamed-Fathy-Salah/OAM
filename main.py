from datetime import date
from schema.base_model import db
from schema.person import Person
from schema.leave import Leave


db.connect()
db.create_tables([Person, Leave])

# Person.create(
        # military_number= '1234123131223',
        # name= 'محمد فتحي صلاح',
        # rank= 'جندي',
        # residence= 'القاهره',
        # brigade= 'ت.أ',
        # demobilization_date= date(year= 2024, month= 3, day= 1),
        # phone_number= '01111234567',
        # national_id= '123412345698034'
        # )

# Leave.create(
    # military_number = "1234123131223",
    # from_date = date(year= 2024, month= 2, day= 1),
    # to_date = date(year= 2024, month= 2, day= 9),
    # travel_form_1 = "12312312",
    # travel_form_2 = "12312321"
    # )

print(Person.select()[:])
print(Leave.select()[:])

