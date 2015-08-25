import peewee
import datetime
from models import Shard

#shard1 = Shard( shard_id = "test_shard_id", last_called_seq_number = "aaaaaaaa", updated_at = datetime.datetime.now() )
#shard = Shard.select().where(Shard.shard_id== "test_shard_id").get()
#shard_krajse = Shard.get(Shard.shard_id == "test_shard_id")

#print(shard)
#print(shard_krajse)
#print(shard.shard_id)
#shard1.save()

shards_all = Shard.select()
shard_number = shards_all.count()
print("Nubmber of shards: ", shard_number)

shard_list = []
shard_id = {}

for shard in shards_all:
    shard_id['shard_id'] = shard.shard_id
    shard_id['last_seq_number'] = shard.last_called_seq_number
    shard_id['updated_at'] = shard.updated_at
    shard_list.append(shard_id)

#print("len od shard_ids ", len(shard_number))
print(shard_list)
