import time
import copy
import heapq
from data import input_data

def calculate_weight(u, t):
    return [t[i] / u[i] for i in range(len(u))]

def sort_weights(weights, u, t):
    zipped = list(zip(weights, u, t))
    sorted_zipped = sorted(zipped, key=lambda x: x[0])
    sorted_weights, u, t = zip(*sorted_zipped)
    return sorted_weights, u, t

def execute_lpt(sorted_weights, m, n, t, u):
    machines = [0] * m
    assigned_jobs = [0] * n

    lpt_schedule = [[] for _ in range(m)]

    for job_index in range(n): #призначає по порядку індекси машини для кожної роботи (0,1,2,2,0)
        machine_index = machines.index(min(machines))
        machines[machine_index] += t[job_index]
        assigned_jobs[job_index] = machine_index

    for i in range(m):
        machine_jobs = [job_index +1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        lpt_schedule[i] = machine_jobs

    return lpt_schedule
