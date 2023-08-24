from datetime import date
from logging import exception
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.errand import Errand
from schema.penalty import Penalty
from schema.base_model import db
from peewee import JOIN

# constants
PRESENT = 'present'
LEAVE = 'leave'
SICK = 'sick'
ERRAND = 'errand'
PRISON = 'prison'
DETENTION = 'DETENTION'
DEFAULT_RETURNING_DAY = date(year= 1900, month= 1, day= 1)

# person
def create_person(
        military_number: str,
        rank: str,
        name: str,
        residence: str,
        brigade: str,
        demobilization_date: date,
        phone_number: str,
        national_id: str
        ):
    try:
        Person.create(
            military_number= military_number,
            rank= rank,
            name= name,
            residence= residence,
            brigade= brigade,
            demobilization_date= demobilization_date,
            phone_number= phone_number,
            national_id= national_id,
            state= PRESENT,
            return_date= date.today()
            )
    except :
        print(f"{rank}/{name} not added")

def remove_person(military_number: str):
    try:
        Person.delete_by_id(military_number)
    except:
        print(f"{military_number} not removed")

def update_person(
        military_number: str,
        rank: str,
        name: str,
        residence: str,
        brigade: str,
        demobilization_date: date,
        phone_number: str,
        national_id: str,
        state: str,
        return_date: date
        ):
    try:
        person = Person.get_by_id(military_number)

        person.name = name
        person.rank = rank
        person.residence= residence
        person.brigade= brigade
        person.demobilization_date= demobilization_date
        person.phone_number= phone_number
        person.national_id= national_id
        person.state= state
        person.return_date= return_date

        person.save()
    except:
        print(f"{military_number} is not updated")

# leave & errand
def create_leave(
        military_number: str,
        from_date: date,
        to_date: date,
        travel_form_1: str,
        travel_form_2: str,
        leave_type: str = LEAVE
        ):
    with db.atomic() as txn:
        try:
            Leave.create(
                military_number= military_number,
                from_date= from_date,
                to_date= to_date,
                return_date= DEFAULT_RETURNING_DAY,
                travel_form_1= travel_form_1,
                travel_form_2= travel_form_2,
                leave_type= leave_type
                    )
            person = Person.get_by_id(military_number)
            person.state= LEAVE
            person.save()
            txn.commit()
        except:
            txn.rollback()
            print(f"{military_number} leave is not added")

def get_leave(leave_id: int):
    try:
        return Leave.select().where(Leave.leave_id == leave_id).dicts()[0]
    except:
        return {}

def get_leaves(military_number: str):
    return Leave.select().where(Leave.military_number == military_number).dicts()[:]

def get_all_leaves():
    return Leave.select().dicts()[:]

def update_leave(
        leave_id: int,
        from_date: date,
        to_date: date,
        return_date: date,
        travel_form_1: str,
        travel_form_2: str,
        leave_type: str
        ):
    with db.atomic() as txn:
        try:
            leave = Leave.get_by_id(leave_id)

            leave.from_date= from_date
            leave.to_date= to_date
            leave.return_date= return_date
            leave.travel_form_1= travel_form_1
            leave.travel_form_2= travel_form_2
            leave.leave_type= leave_type
            leave.save()

            # todo: if last leave update person return_date
            if return_date <= date.today():
                person = Person.get_by_id(leave.military_number)
                person.state = PRESENT
                person.save()
            txn.commit()
        except:
            print(f"leave {leave_id} is not updated")
            txn.rollback()

def remove_leave(leave_id: int, military_number: str):
    with db.atomic() as txn:
        try:
            Leave.delete_by_id(leave_id)
            # todo: check if last leave return_date is set or not
            person = Person.get_by_id(military_number)
            person.state = PRESENT
            person.save()
            txn.commit()
        except:
            txn.rollback()

def create_errand(
        military_number: str,
        from_date: date,
        to_date: date,
        travel_form_1: str,
        travel_form_2: str,
        place: str,
        reason: str
        ):
    with db.atomic() as txn:
        try:
            Errand.create(
                military_number = military_number,
                from_date = from_date,
                to_date = to_date,
                return_date = DEFAULT_RETURNING_DAY,
                travel_form_1 = travel_form_1,
                travel_form_2 = travel_form_2,
                place = place,
                reason = reason
                )

            person = Person.get_by_id(military_number)
            person.state = ERRAND
            person.save()

            txn.commit()
        except:
            print(f"{military_number} errand is not created")
            txn.rollback()

def update_errand(
        errand_id: int,
        from_date: date,
        to_date: date,
        return_date: date,
        travel_form_1: str,
        travel_form_2: str,
        place: str,
        reason: str,
        ):
    with db.atomic() as txn:
        try:
            errand = Errand.get_by_id(errand_id)

            errand.from_date= from_date
            errand.to_date= to_date
            errand.return_date= return_date
            errand.travel_form_1= travel_form_1
            errand.travel_form_2= travel_form_2
            errand.place= place
            errand.reason= reason
            errand.save()

            # todo: if last leave update person return_date
            if return_date <= date.today():
                person = Person.get_by_id(errand.military_number)
                person.state = PRESENT
                person.save()
            txn.commit()
        except:
            print(f"errand {errand_id} is not updated")
            txn.rollback()

def remove_errand(errand_id: int, military_number: str):
    with db.atomic() as txn:
        try:
            Errand.delete_by_id(errand_id)
            # todo: check if last leave return_date is set or not
            person = Person.get_by_id(military_number)
            person.state = PRESENT
            person.save()
            txn.commit()
        except:
            txn.rollback()

def get_errand(errand_id: int):
    try:
        return Errand.select().where(Errand.errand_id == errand_id).dicts()[0]
    except:
        return {}

def get_errands(military_number: str):
    return Errand.select().where(Errand.military_number == military_number).dicts()[:]

def get_all_errands():
    return Errand.select().dicts()[:]

def return_to_base(
        military_number: str,
        day: date
        ):
    with db.atomic() as txn:
        try:
            person = Person.get_by_id(military_number)

            if person.state == LEAVE:
                person.return_date = day
                leave = Leave.get(fn.MAX(Leave.from_date))
                leave.return_date = day
                leave.save()
            elif person.state == ERRAND:
                errand = Errand.get(fn.MAX(Errand.from_date))
                errand.return_date = day
                errand.save()

            person.state = PRESENT

            person.save()

            txn.commit()
        except:
            txn.rollback()

# support
def create_support(
        military_number: str,
        rank: str,
        name: str,
        residence: str,
        brigade: str,
        demobilization_date: date,
        phone_number: str,
        national_id: str,
        detachment: str,
        annexation_date: date
        ):
    with db.atomic() as txn:
        try:
            Person.create(
                military_number= military_number,
                rank= rank,
                name= name,
                residence= residence,
                brigade= brigade,
                demobilization_date= demobilization_date,
                phone_number= phone_number,
                national_id= national_id,
                state= PRESENT,
                return_date= date.today()
                )

            Support.create(
                    military_number= military_number,
                    annexation_date= annexation_date,
                    detachment= detachment
                    )

            txn.commit()
        except :
            txn.rollback()
            print(f"{rank}/{name} not added")

def update_support(
        military_number: str,
        rank: str,
        name: str,
        residence: str,
        brigade: str,
        demobilization_date: date,
        phone_number: str,
        national_id: str,
        state: str,
        return_date: date,
        detachment: str,
        annexation_date: date
        ):

    with db.atomic() as txn:
        try:
            support = Support.get_by_id(military_number)
            support.detachment= detachment
            support.annexation_date= annexation_date

            person = Person.get_by_id(military_number)
            person.rank= rank
            person.name= name
            person.residence= residence
            person.brigade= brigade
            person.demobilization_date= demobilization_date
            person.phone_number= phone_number
            person.national_id= national_id
            person.state= state
            person.return_date= return_date

            support.save()
            person.save()
            txn.commit()
        except:
            txn.rollback()
            print(f"support {rank}/{name} not updated")

def remove_support(
        military_number: str
        ):
    # todo: make delete cascade
    with db.atomic() as txn:
        try:
            Support.delete_by_id(military_number)
            Person.delete_by_id(military_number)
            txn.commit()
        except:
            txn.rollback()
            print(f"{military_number} is not removed")


def create_penalty(
        military_number: str,
        from_date: date,
        to_date: date,
        penalty_type: str
        ):
    try:
        Penalty.create(
                military_number= military_number,
                from_date= from_date,
                to_date= to_date,
                penalty_type= penalty_type
                )
    except:
        print(f"{military_number} penalty is not added")
    

def update_penalty(
        penalty_id: int,
        from_date: date,
        to_date: date,
        penalty_type: str
        ):
    try:
        penalty = Penalty.get_by_id(penalty_id)
        penalty.from_date= from_date
        penalty.to_date= to_date
        penalty.penalty_type= penalty_type
        penalty.save()
    except:
        print(f"penalty {penalty_id} is not updated")

def get_penalty(penalty_id: int):
    try:
        return Penalty.select().where(Penalty.penalty_id == penalty_id).dicts()[0]
    except:
        return {}

def get_penalties():
    return Penalty.select().dicts()[:]

def get_prisoners():
    return Penalty.select().where(Penalty.to_date >= date.today() and Penalty.penalty_type == PRISON).dicts()[:]

def get_detained():
    return Penalty.select().where(Penalty.to_date >= date.today() and Penalty.penalty_type == DETENTION).dicts()[:]

# def get_present():
    # get all person with state = LEAVE & return_date > today

def get_absent():
    return Leave.select().where(Leave.to_date < date.today and Leave.return_date == DEFAULT_RETURNING_DAY).dicts()[:]

def get_sick_leave():
    return Leave.select().where(Leave.to_date >= date.today() and Leave.leave_type == SICK).dicts()[:]

def get_support(military_number: str):
    try:
        return Support.select(Support, Person).join(Person).where(Person.military_number == military_number).dicts()[0]
    except:
        return {}

def get_all_support():
    return Support.select().dicts()[:]

def get_people():
    return Person.select().dicts()[:]

def get_person(military_number: str):
    try:
        return Person.select().where(Person.military_number == military_number).dicts()[0]
    except:
        return {}

# filter peaople by one or more filters
# def filter_peaople(
    # rank = TextField() # todo: make index with name
    # name = CharField() 
    # residence = CharField()
    # brigade = CharField()
    # demobilization_date = DateField()
    # state = CharField() # present, absent, errand
        # ):
