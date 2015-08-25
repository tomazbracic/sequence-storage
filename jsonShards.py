import json


jsonFile = open("shards.json", "r")
shards = json.load(jsonFile)
jsonFile.close()

print("shards read ", shards)


for shard in shards:
    print(shard['shard_id'])
    #print(shards[shard]['shard_id'])
#shards = [
#      {'shard_id': 'shard-0000', 'seq': '123'},
#      {'shard_id': 'shard-0001', 'seq': '456'}
#      ]




jsonFile = open("shards.json", "w+")
jsonFile.write(json.dumps(shards))
jsonFile.close()
