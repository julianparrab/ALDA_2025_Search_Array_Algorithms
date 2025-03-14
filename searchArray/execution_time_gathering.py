import time
import random
from searchArray import algorithms
from searchArray import constants
from searchArray import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size, target):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size, target)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size, target):
    samples = []
    for _ in range(samples_by_size):
        samples.append(sorted(data_generator.get_random_list(size)))
        #print("samples: " + str(samples))
        #print("samples1: " + str(samples[0][random.randint(0, size - 1)]))
        position = random.randint(0, size - 1)
        target = samples[0][position]

    return [
        position,
        take_time_for_algorithm(samples, target, algorithms.linear_search),
        take_time_for_algorithm(samples, target, algorithms.binary_search),
        take_time_for_algorithm(samples, target, algorithms.ternary_search),
        take_time_for_algorithm(samples, target, algorithms.jump_search),
        take_time_for_algorithm(samples, target, algorithms.interpolation_search),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, target, sorting_approach):
    times = []

    for sample in samples_array:
        start_time = time.time()
        pos = sorting_approach(sample.copy(), target)
        #print("pos: " + str(pos))
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
