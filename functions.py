from datetime import date
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.penalty import Penalty
from schema.base_model import db

# constants
PRESENT = 'present'
LEAVE = 'leave'
SICK = 'sick'
ERRAND = 'errand'
PRISON = 'prison'
DETENTION = 'DETENTION'
DEFAULT_RETURNING_DAY = date(year= 1900, month= 1, day= 1)

# person
def add_person(
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
        person.rank = rank,
        person.residence= residence,
        person.brigade= brigade,
        person.demobilization_date= demobilization_date,
        person.phone_number= phone_number,
        person.national_id= national_id
        person.state= state
        person.return_date= return_date

        person.save()
    except:
        print(f"{military_number} is not updated")

# leave & errand
def leave_off(
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

def get_leaves(military_number: str):
    leave = Leave.select().where(Leave.military_number == military_number)
    return leave.dicts()[:]

def get_all_leaves():
    return Leave.select().dicts()

def update_leave(
        leave_id: int,
        military_number: str,
        from_date: date,
        to_date: date,
        return_date: date,
        travel_form_1: str,
        travel_form_2: str,
        leave_type: str
        ):
    try:
        leave = Leave.get_by_id(leave_id)

        leave.military_number = military_number
        leave.from_date= from_date,
        leave.to_date= to_date,
        leave.return_date= return_date,
        leave.travel_form_1= travel_form_1,
        leave.travel_form_2= travel_form_2,
        leave.leave_type= leave_type

        leave.save()
    except:
        print(f"leave {leave_id} is not updated")

def carry_out_errand(
        military_number: str,
        from_date: date,
        to_date: date,
        travel_form_1: str,
        travel_form_2: str,
        place: str,
        reason: str
        ):
    # update person.state = ERRAND 
    # create new errand

# def return_to_base(
        # military_number: str,
        # day: date
        # ):
    # check state
    # if state = LEAVE then update person.return_date = day & leave.return_date = day
    # if state = ERRAND then update errand.to_date = day
    # update person.state = PRESENT

# support
# def add_support(
        # military_number: str,
        # rank: str,
        # name: str,
        # residence: str,
        # brigade: str,
        # demobilization_date: date,
        # phone_number: str,
        # national_id: str,
        # detachment: str,
        # date_of_annexation: date
        # ):
    # create person
    # create support

# def remove_support(
        # military_number: str
        # ):
    # remove person
    # remove support


def add_penalty(
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
    
# def get_prisoners():

# def get_detained():

# def get_sick_leave():

# def get_absent():
    # get all person with state = LEAVE & return_date > today

# def get_all():
    # return Person.get()

# filter peaople by one or more filters
# def filter_peaople(
    # rank = TextField() # todo: make index with name
    # name = CharField() 
    # residence = CharField()
    # brigade = CharField()
    # demobilization_date = DateField()
    # state = CharField() # present, absent, errand
        # ):
