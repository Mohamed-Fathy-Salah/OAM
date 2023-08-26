from peewee import SqliteDatabase, Model

db = SqliteDatabase('OAM.db')
# db = SqliteDatabase(':memory:')

class BaseModel(Model):
    class Meta:
        database = db
