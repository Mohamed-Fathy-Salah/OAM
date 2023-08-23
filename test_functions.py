from functions import *

from datetime import date, timedelta
from peewee import SqliteDatabase
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.errand import Errand
from schema.penalty import Penalty

test_db = SqliteDatabase(':memory:')
test_db.create_tables([Person, Leave, Errand, Penalty, Support])

def test_create_person():
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

def test_update_person():
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
    for i in range(0, 2):
        remove_person(f"133412313122{i}")

    people = get_people()

    # todo: test cascade remove
    assert len(people) == 5 - 2

def test_create_leave():
    for i in range(2, 4):
        for j in range(0, 3):
            create_leave(
                military_number = f"133412313122{i}",
                from_date= date(2023, 10, 1 + j * 5),
                to_date= date(2023, 10, 5 + j * 5),
                travel_form_1= "123123123",
                travel_form_2= "123123233" ,
            )
    assert len(get_all_leaves()) == 6
    assert len(get_leaves("1334123131222")) == 3
    assert len(get_leaves("1334123131223")) == 3
    assert len(get_leaves("1334123131220")) == 0
    assert get_person("1334123131222").state == LEAVE
    assert get_person("1334123131223").state == LEAVE

def test_update_leave():
    leave = get_all_leaves()[0]
    update_leave(
            leave.leave_id,
            from_date= date(2023, 8, 10),
            to_date= date(2023, 8, 29),
            return_date= date.today() + timedelta(days= 1),
            travel_form_1= "123",
            travel_form_2= "124",
            leave_type= SICK
            )

    leave = get_leave(leave.leave_id)
    person = get_person(leave.military_number)

    assert leave.return_date == date.today() + timedelta(days= 1)
    assert person.state == LEAVE

    update_leave(
            leave.leave_id,
            from_date= date(2023, 8, 10),
            to_date= date(2023, 8, 29),
            return_date= date.today(),
            travel_form_1= "123",
            travel_form_2= "124",
            leave_type= SICK
            )
    
    leave = get_leave(leave.leave_id)
    person = get_person(leave.military_number)

    assert leave.return_date == date.today()
    assert person.state == PRESENT
