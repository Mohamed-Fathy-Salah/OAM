from schema.base_model import db
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.errand import Errand
from schema.penalty import Penalty

if __name__ == '__main__':
    db.connect()
    db.create_tables([Person, Leave, Errand, Penalty, Support])
