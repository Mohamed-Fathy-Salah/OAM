from datetime import date
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.errand import Errand
from schema.penalty import Penalty
from constants import *

def get_leave(leave_id: int):
    try:
        return Leave.select().where(Leave.leave_id == leave_id).dicts()[0]
    except:
        return {}

def get_leaves(military_number: str):
    return Leave.select().where(Leave.military_number == military_number).dicts()[:]

def get_all_leaves():
    return Leave.select().dicts()[:]

def get_errand(errand_id: int):
    try:
        return Errand.select().where(Errand.errand_id == errand_id).dicts()[0]
    except:
        return {}

def get_errands(military_number: str):
    return Errand.select().where(Errand.military_number == military_number).dicts()[:]

def get_all_errands():
    return Errand.select().dicts()[:]

def get_penalty(penalty_id: int):
    try:
        return Penalty.select().where(Penalty.penalty_id == penalty_id).dicts()[0]
    except:
        return {}

def get_penalties():
    return Penalty.select().dicts()[:]

def get_prisoners():
    return Penalty.select().where(Penalty.to_date >= date.today(), Penalty.penalty_type == PRISON).dicts()[:]

def get_detained():
    return Penalty.select().where(Penalty.to_date >= date.today(), Penalty.penalty_type == DETENTION).dicts()[:]

def get_present():
    return Person.select().where(Person.state == PRESENT).dicts()[:]

def get_people_in_leave():
    return Person.select().where(Person.state == LEAVE, Person.return_date > date.today()).dicts()[:]

def get_people_in_errand():
    return Person.select().where(Person.state == ERRAND).dicts()[:]

def get_absent():
    leaves = Leave.select().where(Leave.to_date < date.today(), Leave.return_date == DEFAULT_RETURNING_DAY).dicts()[:]
    print(leaves)
    return leaves

def get_sick_leave():
    return Leave.select().where(Leave.to_date >= date.today(), Leave.leave_type == SICK).dicts()[:]

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
