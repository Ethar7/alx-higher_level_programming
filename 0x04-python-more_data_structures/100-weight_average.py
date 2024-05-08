#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    for score, weight in my_list:
        numerator = sum(int(score * weight))
    denominator = sum(weight for _, weight in my_list)

    if denominator == 0:
        return 0

    return numerator / denominator

