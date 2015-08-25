from peewee import *

db = SqliteDatabase('shards.db')

class Shard(Model):
    shard_id = CharField()
    last_called_seq_number = CharField()
    updated_at = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
#db.create_tables([Shard])
db.close()
