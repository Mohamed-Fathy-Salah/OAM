from mutations import *
from queries import *
from constants import *

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
    assert get_person(military_number) == {}

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
    assert person['name'] == name
    assert person['rank'] == rank

def test_remove_person_not_found():
    military_number= "not_a_valid_number"
    remove_person(military_number)

    people = get_people()

    assert len(people) == 5

def test_remove_person():
    for i in range(0, 2):
        remove_person(f"133412313122{i}")

    people = get_people()

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
    assert get_person("1334123131222")['state'] == LEAVE
    assert get_person("1334123131223")['state'] == LEAVE

def test_update_leave():
    leave = get_all_leaves()[0]
    update_leave(
            leave['leave_id'],
            from_date= date(2023, 8, 10),
            to_date= date(2023, 8, 29),
            return_date= date.today() + timedelta(days= 1),
            travel_form_1= "123",
            travel_form_2= "124",
            leave_type= SICK
            )

    leave = get_leave(leave['leave_id'])
    person = get_person(leave['military_number'])

    assert leave['return_date'] == date.today() + timedelta(days= 1)
    assert person['state'] == LEAVE

    update_leave(
            leave['leave_id'],
            from_date= date(2023, 8, 10),
            to_date= date(2023, 8, 29),
            return_date= date.today(),
            travel_form_1= "123",
            travel_form_2= "124",
            leave_type= SICK
            )
    
    leave = get_leave(leave['leave_id'])
    person = get_person(leave['military_number'])

    assert leave['return_date'] == date.today()
    assert person['state'] == PRESENT

def test_remove_leave_not_found():
    remove_leave(leave_id= -1, military_number= "blah")

    assert len(get_all_leaves()) == 6

def test_remove_leave():
    leaves = get_all_leaves()
    for i in range(0, 2):
        remove_leave(leave_id= leaves[i]['leave_id'], military_number= leaves[i]['military_number'])

    assert get_person(leaves[0]['military_number'])['state'] == PRESENT
    assert get_person(leaves[1]['military_number'])['state'] == PRESENT
    assert len(get_all_leaves()) == 6 - 2

def test_create_errand():
    for i in range(2, 4):
        for j in range(0, 3):
            create_errand(
                military_number = f"133412313122{i}",
                from_date= date(2023, 10, 1 + j * 5),
                to_date= date(2023, 10, 5 + j * 5),
                travel_form_1= "123123123",
                travel_form_2= "123123233" ,
                place= 'adsf',
                reason= 'asdf',
            )

    assert len(get_all_errands()) == 6
    assert len(get_errands("1334123131222")) == 3
    assert len(get_errands("1334123131223")) == 3
    assert len(get_errands("1334123131220")) == 0
    assert get_person("1334123131222")['state'] == ERRAND
    assert get_person("1334123131223")['state'] == ERRAND
    
def test_update_errand():
    errand = get_all_errands()[0]
    update_errand(
            errand['errand_id'],
            from_date= date(2023, 8, 10),
            to_date= date(2023, 8, 29),
            return_date= date.today() + timedelta(days= 1),
            travel_form_1= "123",
            travel_form_2= "124",
            place= 'asdf',
            reason= 'adf'
            )

    errand = get_errand(errand['errand_id'])
    person = get_person(errand['military_number'])

    assert errand['return_date']== date.today() + timedelta(days= 1)
    assert person['state']== ERRAND

    update_errand(
            errand_id= errand['errand_id'],
            from_date= date(2023, 8, 10),
            to_date= date(2023, 8, 29),
            return_date= date.today(),
            travel_form_1= "123",
            travel_form_2= "124",
            place= 'adf',
            reason= 'adf'
            )
    
    errand = get_errand(errand['errand_id'])
    person = get_person(errand['military_number'])

    assert errand['return_date']== date.today()
    assert person['state']== PRESENT

def test_remove_errand_not_found():
    remove_errand(errand_id= -1, military_number= "blah")

    assert len(get_all_errands()) == 6

def test_remove_errand():
    errands = get_all_errands()
    for i in range(0, 2):
        remove_errand(errand_id= errands[i]['errand_id'], military_number= errands[i]['military_number'])

    assert get_person(errands[0]['military_number'])['state']== PRESENT
    assert get_person(errands[1]['military_number'])['state']== PRESENT
    assert len(get_all_errands()) == 6 - 2

def test_create_support():
    for i in range(0, 5):
        create_support(
                military_number= f"133412313121{i}",
                name= f"محمد فتحي {i * 5}",
                rank= 'جندي',
                residence= 'القاهره',
                brigade= 'ت.أ',
                demobilization_date= date(year= 2024, month= 3 + i, day= 1),
                phone_number= '01111234567',
                national_id= '123412345698035',
                detachment= 'adf',
                annexation_date= date(year= 2023, month= 3 + i, day= 1)
                )
    assert len(get_all_support()) == 5

def test_update_support_not_found():
    military_number= "not_a_valid_number"
    update_support(
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
            detachment= "adf",
            annexation_date= date(year= 2024, month= 3, day= 1)
    )
    person = get_support(military_number)
    assert person == {}

def test_update_support():
    military_number= "1334123131211"
    name= "محمد"
    rank= 'ملازم'
    update_support(
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
            detachment= 'adf',
            annexation_date= date(year= 2024, month= 3 , day= 1),
        )
    support = get_support(military_number)
    assert support['name'] == name
    assert support['rank'] == rank

def test_remove_support_not_found():
    remove_support(military_number= "blah")

    assert len(get_all_support()) == 5

def test_remove_support():
    support = get_all_support()
    for i in range(0, 2):
        remove_support(military_number= support[i]['military_number'])

    assert len(get_all_support()) == 5 - 2
    assert len(get_people()) == 3 + 3

def test_create_penalty():
    person = get_people()[0]
    create_penalty(
            military_number= person['military_number'],
            from_date= date.today(),
            to_date= date.today() + timedelta(days= 10),
            penalty_type= PRISON
            )
    assert len(get_penalties()) == 1

def test_update_penalty():
    penalty = get_penalties()[0]
    from_date= date.today() + timedelta(days= 10)
    to_date= date.today() + timedelta(days= 20)
    penalty_type= DETENTION

    update_penalty(
            penalty_id= penalty['penalty_id'],
            from_date= from_date,
            to_date= to_date, 
            penalty_type= penalty_type
            )
    penalty = get_penalties()[0]
    assert penalty['from_date'] == from_date
    assert penalty['to_date'] == to_date
    assert penalty['penalty_type'] == penalty_type

def test_get_prisoners():
    person = get_people()[1]
    create_penalty(
            military_number= person['military_number'],
            from_date= date.today() + timedelta(days= -5),
            to_date= date.today() + timedelta(days= 1),
            penalty_type= PRISON
            )
    assert len(get_prisoners()) == 1

def test_get_detained():
    person = get_people()[2]
    create_penalty(
            military_number= person['military_number'],
            from_date= date.today() + timedelta(days= -5),
            to_date= date.today() + timedelta(days= 1),
            penalty_type= DETENTION
            )
    assert len(get_prisoners()) == 1

def test_get_sick_leave():
    person = get_people()[0]
    create_leave(
        military_number = person['military_number'],
        from_date= date.today(),
        to_date= date.today() + timedelta(days= 10),
        travel_form_1= "123123123",
        travel_form_2= "123123233" ,
        leave_type= SICK
    )
    assert len(get_sick_leave()) == 1

def test_get_absent():
    person = get_people()[0]

    old_leaves = get_all_leaves()
    for i in old_leaves:
        remove_leave(leave_id= i['leave_id'], military_number= i['military_number'])

    assert len(get_absent()) == 0

    create_leave(
        military_number = person['military_number'],
        from_date= date.today(),
        to_date= date.today() + timedelta(days= 10),
        travel_form_1= "123123123",
        travel_form_2= "123123233"
    )

    assert len(get_absent()) == 0

    leave = get_all_leaves()[0]

    update_leave(
        leave_id= leave['leave_id'],
        from_date= date.today() + timedelta(days= -10),
        to_date= date.today() + timedelta(days= -1),
        return_date= DEFAULT_RETURNING_DAY,
        travel_form_1= "123123123",
        travel_form_2= "123123233",
        leave_type= LEAVE
    )

    assert len(get_absent()) == 1

    update_leave(
        leave_id= leave['leave_id'],
        from_date= date.today() + timedelta(days= -10),
        to_date= date.today() + timedelta(days= -1),
        return_date= date.today(),
        travel_form_1= "123123123",
        travel_form_2= "123123233",
        leave_type= LEAVE
    )

    assert len(get_absent()) == 0

# def test_return_to_base_from_leave():

# def test_return_to_base_from_errand():

# def test_cascade_remove_person():
    # test remove leaves, errades, support, penalty
