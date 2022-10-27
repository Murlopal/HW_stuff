import json
import random as rand
import numpy as np
data_lists = {}

for i in range(100):
    list_filler = []
    for a in range(100):
        list_filler.append(rand.randrange(9))
    data_lists[i] = list_filler
with open("data_file.json", "w") as write_file:
    json.dump(data_lists, write_file)

print(data_lists)
