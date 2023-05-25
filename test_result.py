import copy
from data import input_data
from lpt_algorithm import calculate_weight, sort_weights, execute_lpt

def find_times_of_jobs(lpt_schedule, t): #час кожної роботи в розкладі
    times_of_jobs = copy.deepcopy(lpt_schedule)
    times_of_jobs = [[t[job_index - 1] for job_index in times_of_jobs[i]] for i in range(len(times_of_jobs))]
    return times_of_jobs

def find_u_of_jobs(lpt_schedule, u): #вага кожної роботи в розкладі
    u_of_jobs = copy.deepcopy(lpt_schedule)
    u_of_jobs = [[u[job_index - 1] for job_index in u_of_jobs[i]] for i in range(len(u_of_jobs))]
    return u_of_jobs

def find_job_ending_time(lpt_schedule, t): #час закінчення кожної роботи в розкладі
    times_of_jobs = find_times_of_jobs(lpt_schedule, t)
    t_end = [] #час закінчення роботи
    for row in  times_of_jobs:
        new_row = []
        summ = 0
        for element in row:
            summ += element
            new_row.append(summ)
        t_end.append(new_row)
    return t_end

def find_total_work_time(lpt_schedule, t):   
    t_end = find_job_ending_time(lpt_schedule, t)
    total_work_time = max(max(t_end, key=max))
    return total_work_time

def find_average_time(lpt_schedule, t, u):
    t_end = find_job_ending_time(lpt_schedule, t)
    u_jobs = find_u_of_jobs(lpt_schedule, u)
    t_u = [[t_end[i][j] * u_jobs[i][j] for j in range(len(t_end[i]))] for i in range(len(t_end))]
    average_time = sum(element for row in t_u for element in row) / sum(u)
    return average_time

def print_results_lpt(lpt_schedule, t, u):
    for i in range(len(lpt_schedule)):
        row = lpt_schedule[i]
        message = f"Машина {i + 1} виконує роботи: {row}"
        print(message)
    times_of_jobs = find_times_of_jobs(lpt_schedule, t)
    for i in range(len(times_of_jobs)):
        row = times_of_jobs[i]
        message = f"В машині {i + 1} часи виконання робіт такі: {row}"
        print(message)
    print("Виведені t:", t)
    print("Виведені u:", u)
    print("Загальний час роботи бригад (в годинах):", find_total_work_time(lpt_schedule, t))
    print("Середній час перебування громадян без світла:", find_average_time(lpt_schedule, t, u))