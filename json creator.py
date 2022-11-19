import json
import random as rand

data_lists = {}
class first:
    filling = {}
    name = ''
class second:
    filling = {}
    name = ''

for i in range(100):
    list_filler = {}
    if i % 2 == 0:
        z = {}
        list_filler = first()
        for a in range(10):
            z[a] = (rand.randrange(10))
        list_filler.filling = z
        list_filler.name = 'type_one'
    else:
        x = {}
        list_filler = second()
        for a in range(10):
            x[a] = (rand.randrange(10))
        list_filler.filling = x
        list_filler.name = 'type_two'

    json_string = json.dumps(list_filler.__dict__)
    data_lists[i] = json_string




with open("data_file.json", "w") as write_file:
    json.dump(data_lists, write_file, indent=4)

print(data_lists)
