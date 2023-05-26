import time
import copy
from data import input_data

# Крок 2 - Розраховуємо ваги за формулою t / u
def calculate_weight(u, t):
    global weights
    weights = [t[i] / u[i] for i in range(len(u))]
    return weights


# Крок 3 - сортуємо знайдені ваги за спаданням
def sort_weights(weights, u, t):
    global sorted_weights
    zipped=list(zip(weights, u, t))
    sorted_zipped = sorted(zipped, key = lambda x: x[0])
    sorted_weights, u, t = list(zip(*sorted_zipped))
    #print("sorted_weights:", ", ".join(f"{weight:.3f}" for weight in sorted_weights))
    return sorted_weights, u, t

# Крок 4 - LPT алгоритм без модифікацій

def execute_lpt(sorted_weights, m, n, t, u):
    machines = [0] * m  # поточна завантаженість машини
    assigned_jobs = [0] * n  #(0,1,2,2,2,0)

    lpt_schedule = [[] for _ in range(m)]   # остаточний розклад

<<<<<<< HEAD
    for job_index in range(len(sorted_weights)):   # призначає по порядку індекси машини для кожної роботи (0,1,2,2,0)
=======
    for job_index in range(len(sorted_weights)): #призначає по порядку індекси машини для кожної роботи (0,1,2,2,0)
>>>>>>> 5495527de865308987c3c4f43eab5a2ce0069921
        machine_index = machines.index(min(machines))
        machines[machine_index] += t[job_index]
        if job_index < n:  # перевірка, чи job_index не виходить за межі списку assigned_jobs
            assigned_jobs[job_index] = machine_index

    for i in range(m):
        machine_jobs = [job_index for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        lpt_schedule[i] = machine_jobs

    return lpt_schedule

