import copy
from data import input_data
from lpt_algorithm import calculate_weight, sort_weights, execute_lpt
from test_result import find_times_of_jobs, find_u_of_jobs, find_job_ending_time, find_total_work_time, find_average_time, print_results_lpt

def insert_job(array, row_index_from, row_index_to, column_index_from_end):
    array_copy = copy.deepcopy(array)
    row1_length = len(array_copy[row_index_from])
    row2_length = len(array_copy[row_index_to])
    column_index_from = row1_length - column_index_from_end - 1
    column_index_to = row2_length - column_index_from_end - 1

    if column_index_from >= 0 and column_index_to >= 0 and column_index_from < row1_length and row_index_from != row_index_to:
        element_to_move = array_copy[row_index_from][column_index_from]
        array_copy[row_index_from].pop(column_index_from)
        array_copy[row_index_to].append(element_to_move)

    return array_copy

def is_2nd_better(array1, array2, t, u):
    total_work_time1 = find_total_work_time(array1, t)
    average_time1 = find_average_time(array1, t, u)

    total_work_time2 = find_total_work_time(array2, t)
    average_time2 = find_average_time(array2, t, u)

    total_time_difference = total_work_time2 - total_work_time1
    average_time_difference = average_time2 - average_time1

    relative_total_time = total_time_difference / min(total_work_time1, total_work_time2)
    relative_average_time = average_time_difference / min(average_time1, average_time2)

    result = relative_average_time + relative_total_time
    if result < 0:
        return True
    else: 
        return False

def execute_lpt_with_job_insertion(sorted_weights, m, n, t, u):
    lpt_schedule = execute_lpt(sorted_weights, m, n, t)  
    for row_index, row in enumerate(lpt_schedule):
        for column_index in range(len(row), -1, -1):
            for next_row_index in range(len(lpt_schedule)):
                if(row_index!=next_row_index):
                    copy_schedule = [list(r) for r in lpt_schedule]
                    copy_schedule = insert_job(copy_schedule, row_index, next_row_index, column_index)
                    if is_2nd_better(lpt_schedule, copy_schedule, t, u):
                        lpt_schedule = [list(r) for r in copy_schedule]


    return lpt_schedule
