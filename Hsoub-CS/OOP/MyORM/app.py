from Model import Model
from Database import Database
from Field import *


Model.db = Database('database.sqlite')
Model.connection = Model.db.connect()

class Post(Model):
    title = CharField()
    body = TextField()
    created_at = DateTimeField()
    published = BooleanField()

class User(Model):
    first_name = CharField()
    last_name = CharField(max_length=225)
    age = IntegerField()


if __name__ == '__main__':
    user = User()
    print(user.get_columns())
