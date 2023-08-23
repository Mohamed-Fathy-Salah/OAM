from datetime import date
from schema.base_model import db
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.errand import Errand
from schema.penalty import Penalty
import functions

db.connect()
db.create_tables([Person, Leave, Errand, Penalty, Support])

military_number= '1334123131223'
functions.create_person(
    military_number= military_number,
    name= 'مصطفي ياسر جلال',
    rank= 'جندي',
    residence= 'القاهره',
    brigade= 'ت.أ',
    demobilization_date= date(year= 2024, month= 3, day= 1),
    phone_number= '01111234567',
    national_id= '123412345698034'
)

# functions.leave_off(
        # military_number= military_number,
        # from_date= date(year=2023, month=8, day=20),
        # to_date= date(year=2023, month=8, day=29),
        # travel_form_1= '12312312',
        # travel_form_2= '12312313'
# )

# print(person.select()[:])

# functions.edit_leave(military_number, new_return_date= date(year=2023, month= 3, day= 11))

# print(Person.select()[:])
print(functions.get_leaves(military_number))
