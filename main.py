import time
from plots import execution_time_plot, diff_amount_m_plot, diff_amount_n_plot, show_plots
from data import input_data
from lpt_algorithm import calculate_weight, sort_weights, execute_lpt
from test_result import find_times_of_jobs, find_u_of_jobs, find_job_ending_time, find_total_work_time, find_average_time, print_results_lpt
from lpt_with_job_insertion import insert_job, execute_lpt_with_job_insertion, is_2nd_better
from lpt_with_pairwise_swapping import swap_jobs, execute_lpt_with_pairwise_swapping    
from lpt_with_job_and_pairwise_swapping import execute_lpt_with_job_and_pairwise_swapping

def main():
    execution_times = []  # Зберігатиме часи виконання для кожного алгоритму
    averages = []
    totals = []
    algorithms = ['lpt', 'lpt with\n job insertion', 'lpt with \npairwise swapping', 'lpt with job\nand pairwise swapping']

    while True:
        option = int(input("Виберіть опцію для розрахування даних за допомогою LPT алгоритму:\n1 - Виконання LPT алгоритму\n2 - Алгоритм LPT з перестановкою робіт з однієї машини на іншу\n3 - Алгоритм LPT з попарними перестановками робіт\n4 - Алгоритм LPT з попарними перестановками робіт та перестановкою робіт з однієї машини на іншу\n5 - Вивести порівняльні графіки \n6 - Вийти з програми\n"))

        if option == 1:
            # Виклик функцій
            option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом, 3 - ввести дані вручну, 4 - зчитування з файлу): "))
            m, n, u, t = input_data(option)
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)

            # Виклик алгоритму
            print("LPT алгоритм:")
            lpt_schedule =execute_lpt(sorted_weights, m, n, t)
            t, a = print_results_lpt(lpt_schedule, t, u)
            end_time = time.time()
            execution_time = end_time - start_time
            print("\nЧас виконання алгоритму: ", execution_time ," секунд") 
            execution_times.append([execution_time])  # Додати час виконання до списку
            averages.append([a])
            totals.append([t])
            
        elif option == 2:
            # Виклик функцій
            option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом, 3 - ввести дані вручну, 4 - зчитування з файлу): "))
            m, n, u, t = input_data(option)
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)


            # Виклик алгоритму
            print("\nLPT Алгоритм з вставленням робіт:")
            lpt_schedule =execute_lpt_with_job_insertion(sorted_weights, m, n, t, u)
            t, a = print_results_lpt(lpt_schedule, t, u)
            end_time = time.time()
            execution_time = end_time - start_time
            print("\nЧас виконання алгоритму: ", execution_time ," секунд") 
            execution_times.append([execution_time])  # Додати час виконання до списку
            averages.append([a])
            totals.append([t])

        elif option == 3:
            # Виклик функцій
            option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом, 3 - ввести дані вручну, 4 - зчитування з файлу): "))
            m, n, u, t = input_data(option)
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)

            # Виклик алгоритму
            print("LPT алгоритм з попарним переставлянням робіт:")
            lpt_schedule =execute_lpt_with_pairwise_swapping(sorted_weights, m, n, t, u)
            t, a = print_results_lpt(lpt_schedule, t, u)
            end_time = time.time()
            execution_time = end_time - start_time
            print("\nЧас виконання алгоритму: ", execution_time ," секунд") 
            execution_times.append([execution_time])  # Додати час виконання до списку
            averages.append([a])
            totals.append([t])

        elif option == 4:
            # Виклик функцій
            option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом, 3 - ввести дані вручну, 4 - зчитування з файлу): "))
            m, n, u, t = input_data(option)
            start_time = time.time()
            weights = calculate_weight(u, t)
            sorted_weights, u, t = sort_weights(weights, u, t)

            # Виклик алгоритму
            print("\nLPT Алгоритм з переставлянням робіт і попарним переставлянням робіт:")
            lpt_schedule =execute_lpt_with_job_and_pairwise_swapping(sorted_weights, m, n, t, u)
            t, a = print_results_lpt(lpt_schedule, t, u)
            end_time = time.time()
            execution_time = end_time - start_time
            print("\nЧас виконання алгоритму: ", execution_time ," секунд") 
            execution_times.append([execution_time])  # Додати час виконання до списку
            averages.append([a])
            totals.append([t])

        elif option == 5:
            # Виклик функції для виводу графіку
            show_plots(algorithms, execution_times)

        elif option == 6:
            # Вихід з програми
            exit(0)
        else:
            #Exception якщо користувач натисне інакшу клавішу
            print("Невірний вибір опції!")
            main

    
main()