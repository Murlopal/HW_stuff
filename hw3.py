import json

import requests
def histDistance(hist1, hist2)->float:
    distance = 0
    sum_square_diff = 0
    for i in range(len(hist1)):
        square_diff = (hist1[i] - hist2[i])**2
        sum_square_diff = sum_square_diff + square_diff
    distance = sum_square_diff**(0.5)
    return distance



with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

