from datetime import date
from schema.person import Person

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
            national_id= national_id
            )
    except :
        print(f"{rank}/{name} not added")

def remove(rank: str, name: str):
    try:
        person = Person.get(rank= rank, name= name) 
        Person.delete_by_id(person.military_number)
    except:
        print(f"{rank}/{name} not removed")

def update(
        old_rank: str,
        old_name: str,
        military_number: str,
        new_rank: str,
        new_name: str,
        residence: str,
        brigade: str,
        demobilization_date: date,
        phone_number: str,
        national_id: str
        ):
    try:
        count = Person.update(name= new_name, rank = new_rank, military_number= military_number, residence= residence, brigade= brigade, demobilization_date= demobilization_date, phone_number= phone_number, national_id= national_id).where(Person.rank == old_rank and Person.name == old_name).execute()
        print(f"{count} rows updated")
    except:
        print(f"{old_rank}/{old_name} not updated")
