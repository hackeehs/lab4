import matplotlib.pyplot as plt
import numpy as np
import random

arr_0 = [int(random.random() * 40) for _ in range(50)]
x = np.arange(0, 50, 1)

def tomorrow_like_yesterday():
    copy_arr_0 = arr_0
    array = [0 for _ in range(len(copy_arr_0))]
    array[0] = copy_arr_0[0]
    for i in range(len(array)):
        if i != 0:
            array[i] = copy_arr_0[i - 1]
    return array

def simple_moving_average():
    array = arr_0.copy()
    window_size = 5
    start_index = 0
    for i in range(len(array)):
        sum = 0
        if i >= window_size - 1:
            counter = start_index
            while counter <= i:
                sum += array[counter]
                counter += 1
            array[i] = sum // window_size
            start_index += 1
    return array

def simple_moving_average_weight():
    array = arr_0.copy()
    window_size = 5
    array_of_weights = [0.85, 0.88, 0.94, 0.96, 0.99]
    start_index = 0
    for i in range(len(array)):
        sum = 0
        if i >= window_size - 1:
            counter = start_index
            weight_index = 0
            while counter <= i:
                sum += int(array[counter] * array_of_weights[weight_index])
                counter += 1
                weight_index += 1
            array[i] = sum // window_size
            start_index += 1
    return array

def exponential():
    copy_arr_0 = arr_0
    array = [0 for _ in range(len(copy_arr_0))]
    alpha = 0.8
    for i in range(len(copy_arr_0)):
        if i == 0:
            array.append(copy_arr_0[i])
        else:
            array[i] = int(array[i - 1] + alpha * (copy_arr_0[i] - array[i - 1]))
    array = array[:-1]
    return array

arr_1 = tomorrow_like_yesterday()
arr_2 = simple_moving_average ()
arr_3 = simple_moving_average_weight()
arr_4 = exponential()

plt.plot(x, arr_0)
print(arr_0)
plt.plot(x, arr_1, 'g')
print(arr_1)
plt.plot(x, arr_2, 'm')
print(arr_2)
plt.plot(x, arr_3, 'r')
print(arr_3)
plt.plot(x, arr_4, 'y')
print(arr_4)
plt.show()

