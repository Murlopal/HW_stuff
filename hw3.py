import json

import requests

r = requests.get('https://api.github.com/events')

r.json()
class first:
    def __init__(self, value_one, value_two):
        self.one = value_one
        self.two = value_two

class second:
    def __init__(self, value_one, value_two):
        self.one = value_one
        self.two = value_two

def histDistance(hist1, hist2)->float:
    distance = 0
    sum_square_diff = 0
    for i in range(len(hist1)):
        square_diff = (hist1[i] - hist2[i])**2
        sum_square_diff = sum_square_diff + square_diff
    distance = sum_square_diff**(0.5)
    return distance

    list_filler[i] = first(value_one=1, value_two=2)
else:
    list_filler[i] = first(value_one=1, value_two=2)


ideal_1 = [0, 8, 8, 4, 2, 2, 6, 8, 8, 3, 1, 4, 5, 2, 6, 4, 3, 4, 0, 3, 8, 3, 6, 4, 5, 7, 5, 6, 6, 5, 0, 8, 0, 8, 3, 7, 0, 5, 0, 5, 8, 2, 5, 1, 6, 2, 4, 1, 1, 2, 8, 0, 2, 1, 4, 3, 3, 2, 4, 3, 7, 2, 6, 6, 1, 8, 0, 4, 5, 1, 7, 1, 1, 5, 3, 2, 8, 7, 8, 4, 2, 6, 8, 1, 3, 7, 3, 0, 7, 4, 1, 3, 8, 4, 3, 0, 6, 1, 3, 7]
ideal_2 = [3, 8, 1, 6, 5, 3, 4, 2, 8, 0, 3, 6, 6, 3, 3, 0, 2, 3, 1, 0, 1, 0, 6, 1, 6, 5, 3, 7, 7, 6, 7, 5, 5, 4, 7, 8, 6, 8, 5, 5, 3, 4, 8, 0, 0, 0, 4, 4, 1, 1, 3, 8, 6, 2, 3, 8, 1, 6, 4, 3, 2, 5, 6, 1, 3, 4, 3, 0, 1, 0, 8, 4, 1, 5, 7, 3, 6, 3, 0, 7, 4, 3, 6, 5, 7, 4, 3, 3, 8, 2, 1, 6, 0, 1, 3, 4, 8, 0, 7, 0]
ideal_3 = [1, 0, 1, 6, 1, 6, 0, 7, 1, 4, 2, 5, 0, 7, 2, 3, 4, 4, 7, 8, 0, 0, 1, 7, 7, 4, 7, 1, 3, 5, 1, 0, 1, 8, 6, 8, 6, 3, 4, 1, 5, 2, 6, 6, 3, 0, 4, 7, 4, 1, 7, 2, 8, 1, 1, 6, 7, 8, 2, 6, 2, 1, 7, 8, 4, 3, 4, 2, 7, 2, 4, 5, 7, 2, 3, 6, 6, 6, 2, 1, 1, 2, 2, 0, 2, 1, 5, 3, 8, 7, 7, 6, 0, 1, 6, 6, 1, 6, 2, 1]

class NNClassifier:
