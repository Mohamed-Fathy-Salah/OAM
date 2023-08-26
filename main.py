from schema.base_model import db
from schema.person import Person
from schema.leave import Leave
from schema.support import Support
from schema.errand import Errand
from schema.penalty import Penalty
import ui

# todo: solve all n+1 query problems
# todo: person state should be tight
if __name__ == '__main__':
    db.connect()
    db.create_tables([Person, Leave, Errand, Penalty, Support])

    ui.run()
