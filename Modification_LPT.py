import random

# Крок 1
def input_data():
    option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом): "))
    if option == 1:
        global m, n, u, t
        m = 3
        n = 10
        u = [53, 25, 30, 80, 24, 55, 25, 5, 90, 38]
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
    print("\nweights =", weights)
    return weights


# Крок 3
def sort_weights(weights):
    global sorted_weights
    sorted_weights = sorted(weights, reverse=True)
    print("\nsorted_weights =", sorted_weights)
    return sorted_weights


# Крок 4
def execute_lpt(sorted_weights, m, n, u, t):
    machines = [0] * m
    assigned_jobs = [0] * n

    for weight in sorted_weights:
        job_index = weights.index(weight)
        machine_index = machines.index(min(machines))
        machines[machine_index] += u[job_index]
        assigned_jobs[job_index] = machine_index

    for i in range(m):
        machine_jobs = [job_index+1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        print("Машина", i + 1, "виконує роботи:", machine_jobs)

    return assigned_jobs


# Крок 5
def print_results_lpt(assigned_jobs, u, t, m):
    max_machine_time = max([sum([t[job_index] for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]) for i in range(m)])
    average_time = sum([t[i] * u[i] for i in range(len(u))]) / sum(u)

    print("\nЗагальний час роботи бригад (в годинах):", max_machine_time)
    print("Середній час перебування громадян без світла при виконанні LPT алгоритму без модифікацій:", average_time)


# Крок 6
def execute_lpt_with_job_swapping(sorted_weights, m, n, u, t):
    machines = [0] * m
    assigned_jobs = [0] * n

    for weight in sorted_weights:
        job_index = weights.index(weight)
        machine_index = machines.index(min(machines))
        machines[machine_index] += u[job_index]
        assigned_jobs[job_index] = machine_index

    iterations = int(input("\nВведіть кількість ітерацій переставляння робіт з однієї мащини на іншу: "))
    improved = True

    while iterations > 0 and improved:
        improved = False

        for i in range(n):
            for j in range(i + 1, n):
                if assigned_jobs[i] != assigned_jobs[j]:
                    current_time = max(machines[assigned_jobs[i]], machines[assigned_jobs[j]])
                    new_time_i = current_time + u[j]
                    new_time_j = current_time + u[i]

                    if new_time_i <= machines[assigned_jobs[j]] and new_time_j <= machines[assigned_jobs[i]]:
                        machines[assigned_jobs[i]] -= u[i]
                        machines[assigned_jobs[j]] -= u[j]
                        machines[assigned_jobs[i]] += u[j]
                        machines[assigned_jobs[j]] += u[i]
                        assigned_jobs[i], assigned_jobs[j] = assigned_jobs[j], assigned_jobs[i]
                        improved = True

        iterations -= 1

    for i in range(m):
        machine_jobs = [job_index+1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        print("Машина", i + 1, "виконує роботи:", machine_jobs)

    return assigned_jobs


# Крок 7
def print_results_lpt_with_job_swapping(assigned_jobs, u, t, m):
    max_machine_time = max([sum([t[job_index] for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]) for i in range(m)])
    average_time = sum([t[i] * u[i] for i in range(len(u))]) / sum(u)

    print("\nЗагальний час роботи бригад (в годинах):", max_machine_time)
    print("Середній час перебування громадян без світла при виконанні LPT алгоритму з перестановкою робіт з однієї машини на іншу:", average_time)

# Крок 8
def execute_lpt_with_pairwise_swapping(sorted_weights, m, n, u, t):
    machines = [0] * m
    assigned_jobs = [0] * n

    for weight in sorted_weights:
        job_index = weights.index(weight)
        machine_index = machines.index(min(machines))
        machines[machine_index] += u[job_index]
        assigned_jobs[job_index] = machine_index

    iterations = int(input("\nВведіть кількість ітерацій попарних переставлянь робіт: "))
    improved = True

    while iterations > 0 and improved:
        improved = False

        for i in range(n):
            for j in range(i + 1, n):
                if assigned_jobs[i] != assigned_jobs[j]:
                    current_time = max(machines[assigned_jobs[i]], machines[assigned_jobs[j]])
                    new_time_i = current_time + u[j]
                    new_time_j = current_time + u[i]

                    if new_time_i <= machines[assigned_jobs[j]] and new_time_j <= machines[assigned_jobs[i]]:
                        machines[assigned_jobs[i]] -= u[i]
                        machines[assigned_jobs[j]] -= u[j]
                        machines[assigned_jobs[i]] += u[j]
                        machines[assigned_jobs[j]] += u[i]
                        assigned_jobs[i], assigned_jobs[j] = assigned_jobs[j], assigned_jobs[i]
                        improved = True

        iterations -= 1

    for i in range(m):
        machine_jobs = [job_index+1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        print("Машина", i + 1, "виконує роботи:", machine_jobs)

    return assigned_jobs


# Крок 9
def print_results_lpt_with_pairwise_swapping(assigned_jobs, u, t, m):
    max_machine_time = max([sum([t[job_index] for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]) for i in range(m)])
    average_time = sum([t[i] * u[i] for i in range(len(u))]) / sum(u)

    print("\nЗагальний час роботи бригад (в годинах):", max_machine_time)
    print("Середній час перебування громадян без світла при виконанні LPT алгоритму з попарними перестановками робіт:", average_time)


# Крок 10
def execute_lpt_with_job_and_pairwise_swapping(sorted_weights, m, n, u, t):
    machines = [0] * m
    assigned_jobs = [0] * n

    for weight in sorted_weights:
        job_index = weights.index(weight)
        machine_index = machines.index(min(machines))
        machines[machine_index] += u[job_index]
        assigned_jobs[job_index] = machine_index

    iterations_job_swapping = int(input("\nВведіть кількість ітерацій переставляння робіт: "))
    iterations_pairwise_swapping = int(input("Введіть кількість ітерацій попарних переставлянь робіт: "))
    improved = True

    while iterations_job_swapping > 0 and improved:
        improved = False

        for i in range(n):
            for j in range(i + 1, n):
                if assigned_jobs[i] != assigned_jobs[j]:
                    current_time = max(machines[assigned_jobs[i]], machines[assigned_jobs[j]])
                    new_time_i = current_time + u[j]
                    new_time_j = current_time + u[i]

                    if new_time_i <= machines[assigned_jobs[j]] and new_time_j <= machines[assigned_jobs[i]]:
                        machines[assigned_jobs[i]] -= u[i]
                        machines[assigned_jobs[j]] -= u[j]
                        machines[assigned_jobs[i]] += u[j]
                        machines[assigned_jobs[j]] += u[i]
                        assigned_jobs[i], assigned_jobs[j] = assigned_jobs[j], assigned_jobs[i]
                        improved = True

        iterations_job_swapping -= 1

    improved = True

    while iterations_pairwise_swapping > 0 and improved:
        improved = False

        for i in range(n):
            for j in range(i + 1, n):
                if assigned_jobs[i] != assigned_jobs[j]:
                    current_time = max(machines[assigned_jobs[i]], machines[assigned_jobs[j]])
                    new_time_i = current_time + u[j]
                    new_time_j = current_time + u[i]
                    if new_time_i <= machines[assigned_jobs[j]] and new_time_j <= machines[assigned_jobs[i]]:
                        machines[assigned_jobs[i]] -= u[i]
                        machines[assigned_jobs[j]] -= u[j]
                        machines[assigned_jobs[i]] += u[j]
                        machines[assigned_jobs[j]] += u[i]
                        assigned_jobs[i], assigned_jobs[j] = assigned_jobs[j], assigned_jobs[i]
                        improved = True

        iterations_pairwise_swapping -= 1

    for i in range(m):
        machine_jobs = [job_index+1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        print("Машина", i + 1, "виконує роботи:", machine_jobs)

    return assigned_jobs


# Крок 11
def print_results_lpt_with_job_and_pairwise_swapping(assigned_jobs, u, t, m):
    max_machine_time = max([sum([t[job_index] for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]) for i in range(m)])
    average_time = sum([t[i] * u[i] for i in range(len(u))]) / sum(u)

    print("\nЗагальний час роботи бригад (в годинах):", max_machine_time)
    print("Середній час перебування громадян без світла при виконанні LPT алгоритму з попарними перестановками робіт та перестановкою робіт з однієї машини на іншу:", average_time)


# якщо не створювати глобальні зміни, єдиний вихід це оголосити локальні змінні ззовні функції, ох уж ці області видимості..
#m, n, u, t = input_data() 
#weights = calculate_weight(u, t)
#sorted_weights = sort_weights(weights)
def main():
    while True:
        option = int(input("\nВиберіть опцію для розрахування даних за допомогою LPT алгоритму:\n1 - Виконання LPT алгоритму\n2 - Алгоритм LPT з перестановкою робіт з однієї машини на іншу\n3 - Алгоритм LPT з попарними перестановками робіт\n4 - Алгоритм LPT з попарними перестановками робіт та перестановкою робіт з однієї машини на іншу\n5 - Вийти з програми\n"))

        if option == 1:
            # Виклик функцій
            m, n, u, t = input_data()
            weights = calculate_weight(u, t)
            sorted_weights = sort_weights(weights)

            # Виклик алгоритму
            print("\nLPT алгоритм:")
            assigned_jobs = execute_lpt(sorted_weights, m, n, u, t)
            print_results_lpt(assigned_jobs, u, t, m)
        elif option == 2:
            # Виклик функцій
            m, n, u, t = input_data()
            weights = calculate_weight(u, t)
            sorted_weights = sort_weights(weights)

            # Виклик алгоритму
            print("\nLPT Алгоритм з переставлянням робіт:")
            assigned_jobs_with_job_swapping = execute_lpt_with_job_swapping(sorted_weights, m, n, u, t)
            print_results_lpt_with_job_swapping(assigned_jobs_with_job_swapping, u, t, m)
        elif option == 3:
            # Виклик функцій
            m, n, u, t = input_data()
            weights = calculate_weight(u, t)
            sorted_weights = sort_weights(weights)

            # Виклик алгоритму
            print("\nLPT Алгоритм з попарним переставлянням робіт:")
            assigned_jobs_with_pairwise_swapping = execute_lpt_with_pairwise_swapping(sorted_weights, m, n, u, t)
            print_results_lpt_with_pairwise_swapping(assigned_jobs_with_pairwise_swapping, u, t, m)
        elif option == 4:
            # Виклик функцій
            m, n, u, t = input_data()
            weights = calculate_weight(u, t)
            sorted_weights = sort_weights(weights)

            # Виклик алгоритму
            print("\nLPT Алгоритм з переставлянням робіт і попарним переставлянням робіт:")
            assigned_jobs_with_job_and_pairwise_swapping = execute_lpt_with_job_and_pairwise_swapping(sorted_weights, m, n, u, t)
            print_results_lpt_with_job_and_pairwise_swapping(assigned_jobs_with_job_and_pairwise_swapping, u, t, m)
        elif option == 5:
            # Вихід з програми
            quit()
        else:
            #Exception якщо користувач натисне інакшу клавішу
            print("Невірний вибір опції!")
            main

main()