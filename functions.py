from datetime import date
from schema.person import Person
from schema.leave import Leave
from schema.base_model import db

# constants
PRESENT = 'present'
LEAVE = 'leave'
ERRAND = 'errand'

DEFAULT_RETURNING_DAY = date(year= 1900, month= 1, day= 1)

# person
def add(
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
            state= PRESENT
            )
    except :
        print(f"{rank}/{name} not added")

def remove(military_number: str):
    try:
        Person.delete_by_id(military_number)
    except:
        print(f"{military_number} not removed")

def update(
        military_number: str,
        rank: str,
        name: str,
        residence: str,
        brigade: str,
        demobilization_date: date,
        phone_number: str,
        national_id: str
        ):
        count = Person.update(name= name, rank = rank, residence= residence, brigade= brigade, demobilization_date= demobilization_date, phone_number= phone_number, national_id= national_id).where(Person.military_number == military_number).execute()
        print(f"{count} rows updated")

# leave
def leave_off(
        military_number: str,
        from_date: date,
        to_date: date,
        travel_form_1: str,
        travel_form_2: str
        ):
    with db.atomic() as txn:
        try:
            Leave.create(
                military_number= military_number,
                from_date= from_date,
                to_date= to_date,
                return_date= DEFAULT_RETURNING_DAY,
                travel_form_1= travel_form_1,
                travel_form_2= travel_form_2
                    )
            Person.update(state= LEAVE).where(Person.military_number == military_number)
            txn.commit()
        except:
            txn.rollback()
            print(f"{military_number} leave is not added")


# def return_to_base(
        # military_number: str,
        # day: date
        # ):
    
