import copy
from data import input_data
from lpt_algorithm import calculate_weight, sort_weights, execute_lpt

def find_times_of_jobs(lpt_schedule, t):
    times_of_jobs = [[t[job_index - 1] if job_index > 0 else 0 for job_index in row] for row in lpt_schedule]
    return times_of_jobs


def find_u_of_jobs(lpt_schedule, u):
    u_of_jobs = [[u[job_index - 1] for job_index in row] for row in lpt_schedule]
    return u_of_jobs


def find_job_ending_time(lpt_schedule, t):
    times_of_jobs = find_times_of_jobs(lpt_schedule, t)
    t_end = []
    for row in times_of_jobs:
        new_row = []
        summ = 0
        for element in row:
            summ += element
            new_row.append(summ)
        t_end.append(new_row)
    return t_end


def find_total_work_time(lpt_schedule, t):
    t_end = find_job_ending_time(lpt_schedule, t)
    total_work_time = max([max(row) for row in t_end if row], default=0)
    return total_work_time


def find_average_time(lpt_schedule, t, u):
    t_end = find_job_ending_time(lpt_schedule, t)
    u_jobs = find_u_of_jobs(lpt_schedule, u)

    t_u = []
    for i in range(len(t_end)):
        row = [t_end[i][j] * u_jobs[i][j] for j in range(len(t_end[i]))]
        t_u.append(row)

    total_time = sum(element for row in t_u for element in row)
    total_weight = sum(u)
    average_time = total_time / total_weight

    return average_time


def print_results_lpt(lpt_schedule, t, u):
    print("Впорядковані t:", t)
    print("Впорядковані u:", u)
    for i in range(len(lpt_schedule)):
        row = lpt_schedule[i]
        message = f"Машина {i + 1} виконує роботи: {row}"
        print(message)
    times_of_jobs = find_times_of_jobs(lpt_schedule, t)
    for i in range(len(times_of_jobs)):
        row = times_of_jobs[i]
        message = f"В машині {i + 1} часи виконання робіт такі: {row}"
        print(message)

        total_work_time = find_total_work_time(lpt_schedule, t)
        average_time = find_average_time(lpt_schedule, t, u)
    print("Загальний час роботи бригад (в годинах):", total_work_time)
    print("Середній час перебування громадян без світла:", average_time)

    return total_work_time, average_time