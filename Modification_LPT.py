from ctypes.wintypes import LPRECT
from gettext import find
import random
import time
import copy
from xml.etree import ElementInclude    

    # Крок 1
def input_data():
    option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом): "))
    if option == 1:
        global m, n, u, t
        m = 3
        n = 10
        u = [53, 25.1, 30, 80, 24, 55, 25, 5, 90, 38]
        t = [5, 2, 3, 6, 2, 5, 2, 1, 7, 4]
    elif option == 2:
        m = int(input("Введіть кількість машин: "))
        n = int(input("Введіть кількість робіт: "))
        u = [random.randint(1, 100) for _ in range(n)]
        t = [random.randint(1, 15) for _ in range(n)]
    else:
        print("Невірний вибір опції!")
        return input_data()

    print("m =", m)
    print("n =", n)
    print("u =", u)
    print("t =", t)    
    return m, n, u, t

# Крок 2
def calculate_weight(u, t):
    global weights
    weights = [t[i] / u[i] for i in range(len(u))]
    return weights


# Крок 3
def sort_weights(weights, u, t):
    global sorted_weights
    zipped=list(zip(weights, u, t))
    sorted_zipped = sorted(zipped, key = lambda x: x[0], reverse=True)
    sorted_weights, u, t = list(zip(*sorted_zipped))
    print("sorted_weights =", ", ".join(f"{weight:.3f}" for weight in sorted_weights))
    return sorted_weights, u, t




# Крок 4
import time
import copy

def execute_lpt(sorted_weights, m, n, t): # видає масив 
    machines = [0] * m #поточна завантаженість машини
    assigned_jobs = [0] * n #(0,1,2,2,2,0)

    lpt_schedule = [[0] * n for _ in range(m)] #остаточний розклад

    for weight in sorted_weights: #призначає по порядку індекси машини для кожної роботи (0,1,2,2,0)
        job_index = sorted_weights.index(weight)
        machine_index = machines.index(min(machines))
        machines[machine_index] += t[job_index]
        assigned_jobs[job_index] = machine_index

    for i in range(m):
        machine_jobs = [job_index + 1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i] #номери роботи в машині 
        lpt_schedule[i] = copy.deepcopy(machine_jobs)

    return lpt_schedule

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
    print("Загальний час роботи бригад (в годинах):", find_total_work_time(lpt_schedule, t))
    print("Середній час перебування громадян без світла:", find_average_time(lpt_schedule, t, u))



def swap_jobs(array, row_index1, row_index2, column_index_from_end):
    array_copy = copy.deepcopy(array)
    row1_length = len(array_copy[row_index1])
    row2_length = len(array_copy[row_index2])
    column_index1 = row1_length - column_index_from_end - 1
    column_index2 = row2_length - column_index_from_end - 1

    if column_index1 >= 0 and column_index2 >= 0 and column_index1 < row1_length and column_index2 < row2_length:
        array_copy[row_index1][column_index1], array_copy[row_index2][column_index2] = array_copy[row_index2][column_index2], array_copy[row_index1][column_index1]

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

def execute_lpt_with_job_insertion(sorted_weights, m, n, t, u):
    lpt_schedule = execute_lpt(sorted_weights, m, n, t)  
    print_results_lpt(lpt_schedule, t, u)
    for row_index in range(len(lpt_schedule)):
        for column_index in range(len(lpt_schedule[row_index]), -1, -1):
            for next_row_index in range (len(lpt_schedule)-1, row_index +1, -1):
                copy_schedule = copy.deepcopy(lpt_schedule)
                copy_schedule = insert_job(copy_schedule, row_index, next_row_index, column_index)
                if is_2nd_better(lpt_schedule, copy_schedule, t, u):
                    lpt_schedule = copy.deepcopy(copy_schedule)


    return lpt_schedule





# Крок 10
def execute_lpt_with_job_and_pairwise_swapping(sorted_weights, m, n, t, u):
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

    for row_index in range(len(lpt_schedule)):
        for column_index in range(len(lpt_schedule[row_index]), -1, -1):
            for next_row_index in range (len(lpt_schedule)-1, row_index +1, -1):
                copy_schedule = copy.deepcopy(lpt_schedule)
                copy_schedule = insert_job(copy_schedule, row_index, next_row_index, column_index)
                if is_2nd_better(lpt_schedule, copy_schedule, t, u):
                    lpt_schedule = copy.deepcopy(copy_schedule)

    return lpt_schedule
    

def main():
    while True:
        option = int(input("Виберіть опцію для розрахування даних за допомогою LPT алгоритму:\n1 - Виконання LPT алгоритму\n2 - Алгоритм LPT з перестановкою робіт з однієї машини на іншу\n3 - Алгоритм LPT з попарними перестановками робіт\n4 - Алгоритм LPT з попарними перестановками робіт та перестановкою робіт з однієї машини на іншу\n5 - Вийти з програми\n"))

        if option == 1:
            # Виклик функцій

            m, n, u, t = input_data()
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)

            # Виклик алгоритму
            print("LPT алгоритм:")
            lpt_schedule =execute_lpt(sorted_weights, m, n, t)
            print_results_lpt(lpt_schedule, t, u)
            end_time = time.time()
            execution_time = end_time - start_time
            print("\nЧас виконання алгоритму: ", execution_time ," секунд") 
            
        elif option == 2:
            # Виклик функцій
            m, n, u, t = input_data()
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)

            # Виклик алгоритму
            print("\nLPT Алгоритм з вставленням робіт:")
            lpt_schedule =execute_lpt_with_job_insertion(sorted_weights, m, n, t, u)
            print_results_lpt(lpt_schedule, t, u)
            end_time = time.time()
            execution_time = end_time - start_time
            print("\nЧас виконання алгоритму: ", execution_time ," секунд") 


        elif option == 3:
            # Виклик функцій

            m, n, u, t = input_data()
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)

            # Виклик алгоритму
            print("LPT алгоритм з попарним переставлянням робіт:")
            lpt_schedule =execute_lpt_with_pairwise_swapping(sorted_weights, m, n, t, u)
            print_results_lpt(lpt_schedule, t, u)
            end_time = time.time()
            execution_time = end_time - start_time
            print("\nЧас виконання алгоритму: ", execution_time ," секунд") 
        elif option == 4:
            # Виклик функцій
            m, n, u, t = input_data()
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)

            # Виклик алгоритму
            print("\nLPT Алгоритм з переставлянням робіт і попарним переставлянням робіт:")
            lpt_schedule =execute_lpt_with_job_and_pairwise_swapping(sorted_weights, m, n, t, u)
            print_results_lpt(lpt_schedule, t, u)
            end_time = time.time()
            execution_time = end_time - start_time
            print("\nЧас виконання алгоритму: ", execution_time ," секунд") 
            
        elif option == 5:
            # Вихід з програми
            quit()
        else:
            #Exception якщо користувач натисне інакшу клавішу
            print("Невірний вибір опції!")
            main

main()