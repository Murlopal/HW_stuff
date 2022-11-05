import json
import random as rand

data_lists = {}


for i in range(100):
    list_filler = []
    for a in range(100):
        list_filler.append(rand.randrange(9))
    data_lists[i] = list_filler
    if (list_filler[i] % 2) == 0:

with open("data_file.json", "w") as write_file:
    json.dump(data_lists, write_file)

print(data_lists)
