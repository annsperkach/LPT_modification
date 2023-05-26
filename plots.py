import matplotlib.pyplot as plt
import math
import time
import random
from statistics import mean 
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

def makespan_plot(algorithms, execution_times):
    # Створення порівняльного графіку за часом виконання алгоритмів
    for i in range(len(algorithms)):
       plt.bar(algorithms[i], execution_times[i])
    plt.xlabel('Алгоритм')
    plt.ylabel('Час роботи бригад')
    plt.title('Порівняння часів роботи бригад')
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
        n=40

        for m in range(2, 21):  # Виконати 20 разів з різними значеннями m
            # Виклик функцій та вимірювання часу виконання
            execution_time_average = []
            for i in range(5):
                print(m, " ",i, end="\r")
                u = [random.randint(1, 100) for _ in range(n)]
                t = [random.randint(1, 15) for _ in range(n)]
                start_time = time.time()
                weights = calculate_weight(u, t)
                sorted_weights, u, t = sort_weights(weights, u, t)
                lpt_schedule = algorithm['function'](sorted_weights, m, n, t, u)
                end_time = time.time()
                execution_time = end_time - start_time
                execution_time_average.append(execution_time)
            execution_times_algorithm.append(mean(execution_time_average))  # Додати час виконання до списку
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
        plt.plot(range(2, 21), execution_times[i], 'o-', label=algorithms[i]['name'])
    plt.xlabel('Кількість машин')
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
        n_values = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]  # Список для збереження значень n
        m = 3

        for n in n_values:
            execution_time_average = []

            # Виклик функцій та вимірювання часу виконання
            for i in range(5):
                u = [random.randint(1, 100) for _ in range(n)]
                t = [random.randint(1, 15) for _ in range(n)]
                print(n, " ",i, end="\r")
                start_time = time.time()
                weights = calculate_weight(u, t)
                sorted_weights, u, t = sort_weights(weights, u, t)
                lpt_schedule = algorithm['function'](sorted_weights, m, n, t, u)
                end_time = time.time()
                execution_time = end_time - start_time
                execution_time_average.append(execution_time)

            execution_times_algorithm.append(execution_time)  # Додати час виконання до списку
 

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
        plt.plot(range(15, 115, 5), execution_times[i], 'o-', label=algorithms[i]['name'])
    plt.xlabel('Кількість робіт')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Залежність часу виконання алгоритмів від кількості робіт')
    plt.legend()  # Додати легенду для алгоритмів
    plt.show()


###########################################################1
def execute_algorithms_m_makespan():
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
        n=40
        
        for m in range(2, 21):  # Виконати 20 разів з різними значеннями m
            # Виклик функцій та вимірювання часу виконання
            execution_time_average = []
            for i in range(5):
                u = [random.randint(1, 100) for _ in range(n)]
                t = [random.randint(1, 15) for _ in range(n)]
                ideal = math.ceil(sum(t)/m)
                print(m, " ",i, end="\r")
                start_time = time.time()
                weights = calculate_weight(u, t)
                sorted_weights, u, t = sort_weights(weights, u, t)
                lpt_schedule = algorithm['function'](sorted_weights, m, n, t, u)

                end_time = time.time()
                execution_time = abs(find_total_work_time(lpt_schedule, t)-ideal)
                execution_time_average.append(execution_time)
            execution_times_algorithm.append(mean(execution_time_average))  # Додати час виконання до списку
            m_values.append(m)  # Додати значення m до списку

        execution_times.append(execution_times_algorithm)  # Додати список часу виконання до загального списку

        # Виведення графіка для поточного алгоритму
        plt.figure()
        plt.plot(m_values, execution_times_algorithm, 'o-')
        plt.xlabel('Значення m')
        plt.ylabel('Відхилення makespan від ідеального')
        plt.title('Залежність відхилення makespan від кількості машин для {}'.format(algorithm['name']))
        plt.show()

    return algorithms, execution_times

def diff_amount_m_plot_makespan(algorithms, execution_times):
    # Створення графіку за часом виконання алгоритму при зміні кількості машин
    for i in range(len(algorithms)):
        plt.plot(range(2, 21), execution_times[i], 'o-', label=algorithms[i]['name'])
    plt.xlabel('Кількість машин')
    plt.ylabel('Відхилення makespan від ідеального')
    plt.title('Порівняльний графік відхилення makespan')
    plt.legend()  # Додати легенду для алгоритмів
    plt.show()


def execute_algorithms_n_makespan():
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
        n_values = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]  # Список для збереження значень n
        m = 3

        for n in n_values:
            execution_time_average = []

            # Виклик функцій та вимірювання часу виконання
            for i in range(5):
                u = [random.randint(1, 100) for _ in range(n)]
                t = [random.randint(1, 15) for _ in range(n)]
                print(n, " ",i, end="\r")
                start_time = time.time()
                ideal = math.ceil(sum(t)/m)
                weights = calculate_weight(u, t)
                sorted_weights, u, t = sort_weights(weights, u, t)
                lpt_schedule = algorithm['function'](sorted_weights, m, n, t, u)
                end_time = time.time()
                execution_time = abs(find_total_work_time(lpt_schedule, t)-ideal)
                execution_time_average.append(execution_time)

            execution_times_algorithm.append(execution_time)  # Додати час виконання до списку
 

        execution_times.append(execution_times_algorithm)  # Додати список часу виконання до загального списку

        # Виведення графіка для поточного алгоритму
        plt.figure()
        plt.plot(n_values, execution_times_algorithm, 'o-')  # Змінено на 'o-' для точок та ліній
        plt.xlabel('Значення n')
        plt.ylabel('Відхилення makespan від ідеального')
        plt.title('Залежність відхилення від кількості робіт для {}'.format(algorithm['name']))
        plt.show()

    return algorithms, execution_times

def diff_amount_n_plot_makespan(algorithms, execution_times):
    # Створення графіку за часом виконання алгоритму при зміні кількості робіт
    for i in range(len(algorithms)):
        plt.plot(range(15, 115, 5), execution_times[i], 'o-', label=algorithms[i]['name'])
    plt.xlabel('Кількість робіт')
    plt.ylabel('Відхилення makespan від ідеального')
    plt.title('Залежність відхилення makespan алгоритмів від кількості робіт')
    plt.legend()  # Додати легенду для алгоритмів
    plt.show()
###########################################################2

def show_plots_execution(algorithms, execution_times):
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
        return show_plots_execution()

def show_plots_makespan(algorithms, execution_times):
  option = int(input("Виберіть вид графіку для виводу: \n1 - Графік порівняння makespan LPT \n2 - Графік порівняння відхилення makespan алгоритмів LPT при зміні кількості машин\n3 - Графік порівняння відхилення makespan алгоритмів LPT при зміні кількості робіт\n"))
  if option == 1:
        makespan_plot(algorithms, execution_times)
  elif option == 2:
        algorithms, execution_times = execute_algorithms_m_makespan()
        diff_amount_m_plot_makespan(algorithms, execution_times)
  elif option == 3:
        algorithms, execution_times = execute_algorithms_n_makespan()
        diff_amount_n_plot_makespan(algorithms, execution_times)

  else:
        print("Невірний вибір опції!")
        return show_plots_execution()