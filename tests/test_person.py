import sys
from datetime import date
from peewee import SqliteDatabase

sys.path.append("..")
from functions import create_person, get_people
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.errand import Errand
from schema.penalty import Penalty

test_db = SqliteDatabase(':memory:')
test_db.create_tables([Person, Leave, Errand, Penalty, Support])

def test_1():
    n = 5
    for i in range(0, n):
        create_person(
            military_number= f"133412313122{i}",
            name= f"محمد فتحي {i}",
            rank= 'جندي',
            residence= 'القاهره',
            brigade= 'ت.أ',
            demobilization_date= date(year= 2024, month= 3 + i, day= 1),
            phone_number= '01111234567',
            national_id= '123412345698035'
        )

    assert len(get_people()) == n

