import json


jsonFile = open("shards.json", "r")
shards = json.load(jsonFile)
jsonFile.close()

print("shards read ", shards)

print(len(shards))

new_shards = []

for shard in shards:
    #for x in range(1, len(shards)):
    print(shard['shard_id'], " in seq je : ", shard['seq'])
    print("star seq", shard['seq'])
    new_seq = int(shard['seq']) + int(shard['seq'])
    print("nov seq", new_seq)

    new_shard = {}

    new_shard['shard_id'] = shard['shard_id']
    new_shard['seq'] = new_seq
    new_shards.append(new_shard)


print(new_shards)


    #print(shards[shard]['shard_id'])
#shards = [
#      {'shard_id': 'shard-0000', 'seq': '123'},
#      {'shard_id': 'shard-0001', 'seq': '456'}
#      ]




jsonFile = open("shards.json", "w+")
jsonFile.write(json.dumps(new_shards))
jsonFile.close()
