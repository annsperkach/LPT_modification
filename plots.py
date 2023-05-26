import matplotlib.pyplot as plt
import time
import random
from data import input_data, read_data_from_file
from lpt_algorithm import calculate_weight, sort_weights, execute_lpt
from test_result import find_times_of_jobs, find_u_of_jobs, find_job_ending_time, find_total_work_time, find_average_time, print_results_lpt
from lpt_with_job_insertion import insert_job, execute_lpt_with_job_insertion, is_2nd_better
from lpt_with_pairwise_swapping import swap_jobs, execute_lpt_with_pairwise_swapping    
from lpt_with_job_and_pairwise_swapping import execute_lpt_with_job_and_pairwise_swapping

def execution_time_plot(algorithms, execution_times):
    # Створення порівняльного графіку за часом виконання алгоритмів
    for i in range(len(algorithms)):
       plt.bar(algorithms[i], execution_times[i])
    plt.xlabel('Алгоритм')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння часу виконання алгоритмів LPT')
    plt.show()

def execute_algorithms_m():
    execution_times = []  # Список для збереження часу виконання
    algorithms = [
        {
            'name': 'LPT алгоритм',
            'function': execute_lpt
        },
        {
            'name': 'LPT алгоритм з вставленням робіт',
            'function': execute_lpt_with_job_insertion
        },
        {
            'name': 'LPT алгоритм з попарним переставлянням робіт',
            'function': execute_lpt_with_pairwise_swapping
        },
        {
            'name': 'LPT алгоритм з переставлянням робіт і попарним переставлянням робіт',
            'function': execute_lpt_with_job_and_pairwise_swapping
        }
    ]

    for algorithm in algorithms:
        execution_times_algorithm = []  # Список для збереження часу виконання для поточного алгоритму
        m_values = []  # Список для збереження значень m

        option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом, 3 - ввести дані вручну, 4 - зчитування з файлу): "))
        m, n, u, t = input_data(option)
        for m in range(1, 21):  # Виконати 20 разів з різними значеннями m
            # Виклик функцій та вимірювання часу виконання
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)
            lpt_schedule = algorithm['function'](sorted_weights, m, n, t, u)
            end_time = time.time()
            execution_time = end_time - start_time

            execution_times_algorithm.append(execution_time)  # Додати час виконання до списку
            m_values.append(m)  # Додати значення m до списку

        execution_times.append(execution_times_algorithm)  # Додати список часу виконання до загального списку

        # Виведення графіка для поточного алгоритму
        plt.figure()
        plt.plot(m_values, execution_times_algorithm, 'o-')
        plt.xlabel('Значення m')
        plt.ylabel('Час виконання (секунди)')
        plt.title('Залежність часу виконання від кількості машин для {}'.format(algorithm['name']))
        plt.show()

    return algorithms, execution_times

def diff_amount_m_plot(algorithms, execution_times):
    # Створення графіку за часом виконання алгоритму при зміні кількості машин
    for i in range(len(algorithms)):
        plt.plot(range(1, 21), execution_times[i], 'o-', label=algorithms[i]['name'])
    plt.xlabel('Значення m')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняльний графік часу виконання алгоритмів')
    plt.legend()  # Додати легенду для алгоритмів
    plt.show()


def execute_algorithms_n():
    execution_times = []  # Список для збереження часу виконання
    algorithms = [
        {
            'name': 'LPT алгоритм',
            'function': execute_lpt
        },
        {
            'name': 'LPT алгоритм з вставленням робіт',
            'function': execute_lpt_with_job_insertion
        },
        {
            'name': 'LPT алгоритм з попарним переставлянням робіт',
            'function': execute_lpt_with_pairwise_swapping
        },
        {
            'name': 'LPT алгоритм з переставлянням робіт і попарним переставлянням робіт',
            'function': execute_lpt_with_job_and_pairwise_swapping
        }
    ]

    

    for algorithm in algorithms:
        execution_times_algorithm = []  # Список для збереження часу виконання для поточного алгоритму
        n_values = []  # Список для збереження значень n
        option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом, 3 - ввести дані вручну, 4 - зчитування з файлу): "))
        m, n, u, t = input_data(option)  # Приймати значення m, n, u, t з функції input_data(option)

        for n in range(1, 21):
            t = list(t)  # Перетворити кортеж t на список
            u = list(u)
            if n > len(t):  # Якщо n більше поточної довжини t, додати додаткові значення t і u
                extra_t = [random.randint(1, 15) for _ in range(n - len(t))]
                extra_u = [random.randint(1, 100) for _ in range(n - len(t))]
                t.extend(extra_t)
                u.extend(extra_u)
            t = tuple(t)  # Перетворити список t на кортеж знову
            u = tuple(u)

            # Виклик функцій та вимірювання часу виконання
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)
            lpt_schedule = algorithm['function'](sorted_weights, m, n, t, u)
            end_time = time.time()
            execution_time = end_time - start_time

            execution_times_algorithm.append(execution_time)  # Додати час виконання до списку
            n_values.append(n)  # Додати значення n до списку

        execution_times.append(execution_times_algorithm)  # Додати список часу виконання до загального списку

        # Виведення графіка для поточного алгоритму
        plt.figure()
        plt.plot(n_values, execution_times_algorithm, 'o-')  # Змінено на 'o-' для точок та ліній
        plt.xlabel('Значення n')
        plt.ylabel('Час виконання (секунди)')
        plt.title('Залежність часу виконання від кількості робіт для {}'.format(algorithm['name']))
        plt.show()

    return algorithms, execution_times

def diff_amount_n_plot(algorithms, execution_times):
    # Створення графіку за часом виконання алгоритму при зміні кількості робіт
    for i in range(len(algorithms)):
        plt.plot(range(1, 21), execution_times[i], 'o-', label=algorithms[i]['name'])
    plt.xlabel('Кількість машин')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Залежність часу виконання алгоритмів від кількості робіт')
    plt.legend()  # Додати легенду для алгоритмів
    plt.show()

def show_plots(algorithms, execution_times):
  option = int(input("Виберіть вид графіку для виводу: \n1 - Графік порівняння часу виконання алгоритмів LPT \n2 - Графік порівняння часу виконання алгоритмів LPT при зміні кількості машин\n3 - Графік порівняння часу виконання алгоритмів LPT при зміні кількості робіт\n"))
  if option == 1:
        execution_time_plot(algorithms, execution_times)
  elif option == 2:
        algorithms, execution_times = execute_algorithms_m()
        diff_amount_m_plot(algorithms, execution_times)
  elif option == 3:
        algorithms, execution_times = execute_algorithms_n()
        diff_amount_n_plot(algorithms, execution_times)
  else:
        print("Невірний вибір опції!")
        return show_plots()