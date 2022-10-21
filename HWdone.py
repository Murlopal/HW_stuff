# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time



import numpy as np

data_list = np.random.randint(0, 999, size=1000000)
sorted_list = sorted(data_list)


def calcHist():

    b = sorted_list
    hist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):

        var_num_start = i * 100
        var_num_end = (i+1) * 100
        if var_num_end == 1000:
            i1 = b.index(var_num_start)
            i2 = 999999
        else:
            i1 = b.index(var_num_start)
            i2 = b.index(var_num_end) - 1
        hist[i] = (i2 - i1)
        b = b[i2:]
    return hist


def one_time_bit():

    # starting time

    start = time.time()

    calcHist()

    # end time

    end = time.time()

    # total time taken

    return (end - start)


print(list(calcHist()))

print("Runtime of the one_time_bit is ", one_time_bit())

def time_stats():
    time_max = 0
    time_all = 0
    time_min = 9999

    for i in range(100):
        times = one_time_bit()
        if times > time_max:
            time_max = times
        elif times < time_min:
            time_min = times
        time_all = time_all + times
    return ("max time=", time_max, "min time =", time_min, "avg time =", time_all/100)

print(time_stats())

