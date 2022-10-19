# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy



def triangle(a):
    for dot in range(a+1):
        print((a-dot)*' '+((dot*2)+1)*'*')


def histDistanve(hist1, hist2)->float:
    distance = 0
    sum_square_diff = 0
    for i in range(len(hist1)):
        square_diff = (hist1[i] - hist2[i])**2
        sum_square_diff = sum_square_diff + square_diff
    distance = sum_square_diff**(0.5)
    return distance

def record(hist1, hist2):
    hist1 = ''
    hist2 = ''
    input(hist1)
    input(hist2)

    with open('hist1', 'w') as hist1:
        hist1.write
    open('hist2', 'w')



