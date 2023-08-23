from logging import log
import sys
from datetime import date
from peewee import SqliteDatabase

sys.path.append("..")
from functions import *
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.errand import Errand
from schema.penalty import Penalty

test_db = SqliteDatabase(':memory:')
test_db.create_tables([Person, Leave, Errand, Penalty, Support])

for i in range(0, 5):
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

def test_create():
    assert len(get_people()) == 5

def test_update_person_not_found():
    military_number= "not_a_valid_number"
    update_person(
            military_number= military_number,
            name= 'adsf',
            rank= 'adfad',
            residence= 'القاهره',
            brigade= 'ت.أ',
            demobilization_date= date(year= 2024, month= 3 , day= 1),
            phone_number= '01111234567',
            national_id= '123412345698035',
            state= PRESENT,
            return_date= date(year= 2023, month= 3 , day= 1),
    )
    person = get_person(military_number)
    assert person == None

def test_update():
    military_number= "1334123131221"
    name= "محمد"
    rank= 'ملازم'
    update_person(
            military_number= military_number,
            name= name,
            rank= rank,
            residence= 'القاهره',
            brigade= 'ت.أ',
            demobilization_date= date(year= 2024, month= 3 , day= 1),
            phone_number= '01111234567',
            national_id= '123412345698035',
            state= PRESENT,
            return_date= date(year= 2023, month= 3 , day= 1),
    )
    person = get_person(military_number)
    assert person.name == name
    assert person.rank == rank

def test_remove_person_not_found():
    military_number= "not_a_valid_number",
    remove_person(military_number)

    people = get_people()

    assert len(people) == 5

def test_remove_person():
    military_number= "",

    for i in range(0, 2):
        remove_person(f"133412313122{i}")

    people = get_people()

    assert len(people) == 5 - 2
