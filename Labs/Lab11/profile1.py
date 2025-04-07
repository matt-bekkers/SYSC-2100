# SYSC 2100 Winter 2024 - Lab 12

# Put import statements here.

__author__ = 'Matthé Bekkers'
__student_number__ = '101297066'

from time import perf_counter
from sort1 import *
import generate_data1
from random import randint, choice
from copy import deepcopy

# Your profiling functions can have as many parameters as you want.
# The return type of each function is up to you.


LIST_LENGTH = 9999

def profile_bubble_sort(list_:list)->None:
    print("Profiling bubble sort")
    # Apply sort
    start_time = perf_counter()
    bubble_sort(list_, len(list_))
    end_time = perf_counter()
    
    # Print sorting time
    total_time = end_time - start_time
    print(f"\t Time: {total_time:.3f} sec")

    # Discard local variables
    del start_time
    del end_time
    del total_time

def profile_selection_sort(list_:list):
    # Please implement the profile function in a similar way to bubble sort
    print("Profiling selection sort")

    start_time = perf_counter()
    selection_sort(list_, len(list_))
    end_time = perf_counter()

    total_time = end_time - start_time
    print(f"\t Time: {total_time:.3f} sec")

    del start_time
    del end_time
    del total_time


def profile_insertion_sort(list_:list):
    # Please implement the profile function in a similar way to bubble sort
    print("Profiling insertion sort")

    start_time = perf_counter()
    insertion_sort(list_, len(list_))
    end_time = perf_counter()

    total_time = end_time - start_time
    print(f"\t Time: {total_time:.3f} sec")

    del start_time
    del end_time
    del total_time

def profile_heapsort(list_:list):
    # Please implement the profile function in a similar way to bubble sort
    print("Profiling heap sort")

    start_time = perf_counter()
    heapsort(list_, len(list_))
    end_time = perf_counter()

    total_time = end_time - start_time
    print(f"\t Time: {total_time:.3f} sec")

    del start_time
    del end_time
    del total_time

def profile_merge_sort(list_:list):
    # Please implement the profile function in a similar way to bubble sort
    print("Profiling merge sort")

    start_time = perf_counter()
    merge_sort(list_, len(list_))
    end_time = perf_counter()

    total_time = end_time - start_time
    print(f"\t Time: {total_time:.3f} sec")

    del start_time
    del end_time
    del total_time

def profile_quicksort(list_:list):
    # Please implement the profile function in a similar way to bubble sort
    print("Profiling quick sort")

    start_time = perf_counter()
    quick_sort(list_, len(list_))
    end_time = perf_counter()

    total_time = end_time - start_time
    print(f"\t Time: {total_time:.3f} sec")

    del start_time
    del end_time
    del total_time


def run_profiles(list_:list):
    # deep copy is used so that the mutated list is not passed to the other sorting algorithms
    profile_selection_sort(deepcopy(list_))
    profile_insertion_sort(deepcopy(list_))
    profile_bubble_sort(deepcopy(list_))
    profile_merge_sort(deepcopy(list_))
    profile_heapsort(deepcopy(list_))
    try:  
        profile_quicksort(deepcopy(list_)) # if the list is too large the recursive depth is reached
    except Exception as e:
        print(f"Quick sort max depth reached... error:{e}")


# You are permitted to change this script.
if __name__ == '__main__':
    print(f"\n\nRunning profiles for randomly sorted list")
    list_ = generate_data1.generate_random_list(LIST_LENGTH)
    run_profiles(list_)
    del list_


    print(f"\n\nRunning profiles for nearly sorted list")
    # generate data with nearly sorted values and run the profile function 'run_profiles'
    list_ = generate_data1.generate_nearly_sorted_list(LIST_LENGTH)
    run_profiles(list_)
    del list_

    print(f"\n\nRunning profiles for a list with few unique")
    # generate data with nearly sorted values and run the profile function 'run_profiles'
    list_ = generate_data1.generate_few_unique_list(LIST_LENGTH)
    run_profiles(list_)
    del list_

    print(f"\n\nRunning profiles for reverse sorted list")
    # generate data with nearly sorted values and run the profile function 'run_profiles'
    list_ = generate_data1.generate_reverse_sorted_list(LIST_LENGTH)
    run_profiles(list_)
    del list_