from peewee import SqliteDatabase, Model

db = SqliteDatabase('OAM.db')

class BaseModel(Model):
    class Meta:
        database = db
