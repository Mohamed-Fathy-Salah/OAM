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

# Leave.create(
    # military_number = "1234123131223",
    # from_date = date(year= 2024, month= 2, day= 1),
    # to_date = date(year= 2024, month= 2, day= 9),
    # travel_form_1 = "12312312",
    # travel_form_2 = "12312321"
    # )
# Support.create(
    # military_number = "1234123131223",
    # date_of_annexation = date(year=2024, month=1, day= 20),
    # detachment = "ك785"
        # )


functions.add(
    military_number= '1334123131223',
    name= 'مصطفي ياسر جلال',
    rank= 'جندي',
    residence= 'القاهره',
    brigade= 'ت.أ',
    demobilization_date= date(year= 2024, month= 3, day= 1),
    phone_number= '01111234567',
    national_id= '123412345698034'
)


print(Person.select()[:])

functions.update(
        old_rank= 'ملازم',
        old_name= 'محمد فتحي صلاح', 
        military_number= '1334123131223',
        new_rank= 'لواء',
        new_name= 'محمد فتحي صلاح', 
        residence= 'اسكندريه',
        brigade= 'ت.أ',
        demobilization_date= date(year= 2024, month= 3, day= 1),
        phone_number= '01111234567',
        national_id= '123412345698034'
                 )

print(Person.select()[:])
# print(Leave.select()[:])
# print(Support.select()[:])
