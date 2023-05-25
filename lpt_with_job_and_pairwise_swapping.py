import copy 

from data import input_data
from lpt_algorithm import calculate_weight, sort_weights, execute_lpt
from test_result import find_times_of_jobs, find_u_of_jobs, find_job_ending_time, find_total_work_time, find_average_time, print_results_lpt
from lpt_with_job_insertion import insert_job, execute_lpt_with_job_insertion, is_2nd_better
from lpt_with_pairwise_swapping import swap_jobs, execute_lpt_with_pairwise_swapping   



def execute_lpt_with_job_and_pairwise_swapping(sorted_weights, m, n, t, u):
    lpt_schedule = execute_lpt(sorted_weights, m, n, t)

    for row_index, row in enumerate(lpt_schedule):
        for column_index in range(len(row), -1, -1):
            for next_row_index in range(len(lpt_schedule) - 1, row_index + 1, -1):
                copy_schedule = [list(r) for r in lpt_schedule]
                copy_schedule = swap_jobs(copy_schedule, row_index, next_row_index, column_index)
                if is_2nd_better(lpt_schedule, copy_schedule, t, u):
                    lpt_schedule = [list(r) for r in copy_schedule]
                copy_schedule = [list(r) for r in lpt_schedule]
                copy_schedule = insert_job(copy_schedule, row_index, next_row_index, column_index)
                if is_2nd_better(lpt_schedule, copy_schedule, t, u):
                    lpt_schedule = [list(r) for r in copy_schedule]

    return lpt_schedule

