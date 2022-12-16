import json

import requests


def histDistance(hist1, hist2) -> float:
    distance = 0
    sum_square_diff = 0
    for i in range(len(hist1)):
        square_diff = (hist1[i] - hist2[i]) ** 2
        sum_square_diff = sum_square_diff + square_diff
    distance = sum_square_diff ** (0.5)
    return distance


r = requests.get("https://raw.githubusercontent.com/Murlopal/HW_stuff/main/data_file.json")
file_base = json.loads(r.text)
print(file_base['2'])




class dist_mes:
    dist = 0
    type_name = ''


def json_untangler_filling(key):
    def intersection(lst1, lst2):
        # Use of hybrid method
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        return lst3

    another_list = []
    for i in range(13, 93):  # only works with histogramms made of 10 numbers. Can be easily fixed
        another_list.append(file_base[f"{key}"][i])
    values = list(map(int, (intersection(another_list, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))))
    return (values[1::2])


def json_untangler_name(key):
    another_list = []
    for i in range(103, 111):
        another_list.append(file_base[f'{key}'][i])
    return ''.join(another_list)




class NNClassifier:

    def __init__(self, filling):
        self.filling = filling


    def type_finder(self):

        first_dist = dist_mes()
        first_dist.dist = 99999999

        second_dist = dist_mes()
        second_dist.dist = 99999999

        third_dist = dist_mes()
        third_dist.dist = 99999999

        for e in range(len(file_base) - 1):
            if histDistance(self.filling, json_untangler_filling(e)) == 0:
                first_dist.dist = 0
                first_dist.type_name = json_untangler_name(e)
            elif histDistance(self.filling, json_untangler_filling(e)) < first_dist.dist:
                third_dist.dist = second_dist.dist
                third_dist.type_name = second_dist.type_name
                second_dist.dist = first_dist.dist
                second_dist.type_name = first_dist.type_name
                first_dist.dist = histDistance(self.filling, json_untangler_filling(e))
                first_dist.type_name = json_untangler_name(e)
        if first_dist.type_name == second_dist.type_name or third_dist.type_name:
            return first_dist.type_name
        else:
            return second_dist.type_name


print(NNClassifier([9,9,3,4,9,6,7,8,9,0]).type_finder())