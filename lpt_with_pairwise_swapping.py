import copy
from data import input_data
from lpt_algorithm import calculate_weight, sort_weights, execute_lpt
from test_result import find_times_of_jobs, find_u_of_jobs, find_job_ending_time, find_total_work_time, find_average_time, print_results_lpt
from lpt_with_job_insertion import insert_job, execute_lpt_with_job_insertion, is_2nd_better

def swap_jobs(array, row_index1, row_index2, column_index_from_end):
    array_copy = copy.deepcopy(array)
    row1_length = len(array_copy[row_index1])
    row2_length = len(array_copy[row_index2])
    column_index1 = row1_length - column_index_from_end - 1
    column_index2 = row2_length - column_index_from_end - 1

    if column_index1 >= 0 and column_index2 >= 0 and column_index1 < row1_length and column_index2 < row2_length:
        array_copy[row_index1][column_index1], array_copy[row_index2][column_index2] = array_copy[row_index2][column_index2], array_copy[row_index1][column_index1]

    return array_copy

# Крок 8
def execute_lpt_with_pairwise_swapping(sorted_weights, m, n, t, u):
    lpt_schedule = execute_lpt(sorted_weights, m, n, t)  
    print("\nПопередні результати:")
    print_results_lpt(lpt_schedule, t, u)
    
    for row_index in range(len(lpt_schedule)):
        for column_index in range(len(lpt_schedule[row_index]), -1, -1):
            for next_row_index in range (len(lpt_schedule)-1, row_index +1, -1):
                copy_schedule = copy.deepcopy(lpt_schedule)
                copy_schedule = swap_jobs(copy_schedule, row_index, next_row_index, column_index)
                if is_2nd_better(lpt_schedule, copy_schedule, t, u):
                    lpt_schedule = copy.deepcopy(copy_schedule)
    return lpt_schedule

