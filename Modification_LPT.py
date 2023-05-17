import random

# Крок 1
def input_data():
    option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом): "))
    if option == 1:
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
        return None

    print("m =", m)
    print("n =", n)
    print("u =", u)
    print("t =", t)

    return m, n, u, t


# Крок 2
def calculate_weight(u, t):
    weights = [t[i] / u[i] for i in range(len(u))]
    print("weights =", weights)
    return weights


# Крок 3
def sort_weights(weights):
    sorted_weights = sorted(weights, reverse=True)
    print("sorted_weights =", sorted_weights)
    return sorted_weights


# Крок 4
def execute_lpt(sorted_weights, m, n, u, t):
    machines = [0] * m
    assigned_jobs = [None] * n

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
def print_results_lpt(assigned_jobs, u, t):
    max_machine_time = max([sum([t[job_index] for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]) for i in range(m)])
    average_time = sum([t[i] * u[i] for i in range(len(u))]) / sum(u)

    print("Загальний час роботи бригад (в годинах):", max_machine_time)
    print("Середній час перебування громадян без світла при виконанні LPT алгоритму без модифікацій:", average_time)


# Крок 6
def execute_lpt_with_job_swapping(sorted_weights, m, n, u, t):
    machines = [0] * m
    assigned_jobs = [None] * n

    for weight in sorted_weights:
        job_index = sorted_weights.index(weight)
        machine_index = machines.index(min(machines))
        machines[machine_index] += u[job_index]
        assigned_jobs[job_index] = machine_index

    iterations = int(input("Введіть кількість ітерацій переставляння робіт з однієї машини на іншу: "))
    improved = True

    while iterations > 0 and improved:
        improved = False

        for i in range(n):
            for j in range(i + 1, n):
                if assigned_jobs[i] != assigned_jobs[j]:
                    if assigned_jobs[i] is not None and assigned_jobs[j] is not None:
                       current_time = max(machines[assigned_jobs[i]], machines[assigned_jobs[j]])
                    new_time_i = current_time + u[job_index] 
                    new_time_j = current_time + u[j]
                    if assigned_jobs[i] is not None and assigned_jobs[j] is not None:
                      if new_time_i <= machines[assigned_jobs[j]] and new_time_j <= machines[assigned_jobs[i]]:
                        machines[assigned_jobs[i]] -= u[job_index]
                        machines[assigned_jobs[j]] -= u[j]
                        machines[assigned_jobs[i]] += u[j]
                        machines[assigned_jobs[j]] += u[job_index]
                        assigned_jobs[i], assigned_jobs[j] = assigned_jobs[j], assigned_jobs[i]
                        improved = True

        iterations -= 1

    for i in range(m):
        machine_jobs = [job_index+1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        print("Машина", i + 1, "виконує роботи:", machine_jobs)

    return assigned_jobs


# Крок 7
def print_results_lpt_with_job_swapping(assigned_jobs, u, t):
    max_machine_time = max([sum([t[job_index] for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]) for i in range(m)])
    average_time = sum([t[i] * u[i] for i in range(len(u))]) / sum(u)

    print("Загальний час роботи бригад (в годинах):", max_machine_time)
    print("Середній час перебування громадян без світла при виконанні LPT алгоритму з перестановкою робіт з однієї машини на іншу:", average_time)


    # Крок 8
def execute_lpt_with_pairwise_swapping(sorted_weights, m, n, u, t):
    machines = [0] * m
    assigned_jobs = [None] * n

    for weight in sorted_weights:
        job_index = sorted_weights.index(weight)
        machine_index = machines.index(min(machines))
        machines[machine_index] += u[job_index]
        assigned_jobs[job_index] = machine_index

    iterations = int(input("Введіть кількість ітерацій попарних переставлянь робіт: "))
    improved = True

    while iterations > 0 and improved:
        improved = False

        for i in range(n):
            for j in range(i + 1, n):
                if assigned_jobs[i] is not None and assigned_jobs[j] is not None:
                 if assigned_jobs[i] != assigned_jobs[j]:
                    current_time = max(machines[assigned_jobs[i]], machines[assigned_jobs[j]])
                    new_time_i = current_time + u[job_index]
                    new_time_j = current_time + u[j]
                    if assigned_jobs[i] is not None and assigned_jobs[j] is not None:
                     if new_time_i <= machines[assigned_jobs[j]] and new_time_j <= machines[assigned_jobs[i]]:
                        machines[assigned_jobs[i]] -= u[job_index]
                        machines[assigned_jobs[j]] -= u[j]
                        machines[assigned_jobs[i]] += u[j]
                        machines[assigned_jobs[j]] += u[job_index]
                        assigned_jobs[i], assigned_jobs[j] = assigned_jobs[j], assigned_jobs[i]
                        improved = True

        iterations -= 1

    for i in range(m):
        machine_jobs = [job_index+1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        print("Машина", i + 1, "виконує роботи:", machine_jobs)

    return assigned_jobs

# Крок 9
def print_results_lpt_with_pairwise_swapping(assigned_jobs, u, t):
    max_machine_time = max([sum([t[job_index] for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]) for i in range(m)])
    average_time = sum([t[i] * u[i] for i in range(len(u))]) / sum(u)

    print("Загальний час роботи бригад (в годинах):", max_machine_time)
    print("Середній час перебування громадян без світла при виконанні LPT алгоритму з попарними перестановками робіт:", average_time)


# Крок 10
def execute_lpt_with_job_and_pairwise_swapping(sorted_weights, m, n, u, t):
    machines = [0] * m
    assigned_jobs = [None] * n

    for weight in sorted_weights:
        job_index = sorted_weights.index(weight)
        machine_index = machines.index(min(machines))
        machines[machine_index] += u[job_index]
        assigned_jobs[job_index] = machine_index

    iterations_job_swapping = int(input("Введіть кількість ітерацій переставляння робіт з однієї машини на іншу: "))
    iterations_pairwise_swapping = int(input("Введіть кількість ітерацій попарних переставлянь робіт: "))

    improved = True

    while iterations_job_swapping > 0 and improved:
        improved = False

        for i in range(n):
            for j in range(i + 1, n):
                if assigned_jobs[i] is not None and assigned_jobs[j] is not None:
                 if assigned_jobs[i] != assigned_jobs[j]:
                    current_time = max(machines[assigned_jobs[i]], machines[assigned_jobs[j]])
                    new_time_i = current_time + u[job_index]
                    new_time_j = current_time + u[j]
                    if assigned_jobs[i] is not None and assigned_jobs[j] is not None:
                     if new_time_i <= machines[assigned_jobs[j]] and new_time_j <= machines[assigned_jobs[i]]:
                        machines[assigned_jobs[i]] -= u[job_index]
                        machines[assigned_jobs[j]] -= u[j]
                        machines[assigned_jobs[i]] += u[j]
                        machines[assigned_jobs[j]] += u[job_index]
                        assigned_jobs[i], assigned_jobs[j] = assigned_jobs[j], assigned_jobs[i]
                        improved = True

        iterations_job_swapping -= 1

    improved = True

    while iterations_pairwise_swapping > 0 and improved:
        improved = False

        for i in range(n):
            for j in range(i + 1, n):
                if assigned_jobs[i] is not None and assigned_jobs[j] is not None:
                 if assigned_jobs[i] != assigned_jobs[j]:
                    current_time = max(machines[assigned_jobs[i]], machines[assigned_jobs[j]])
                    new_time_i = current_time + u[job_index]
                    new_time_j = current_time + u[j]

                    if assigned_jobs[i] is not None and assigned_jobs[j] is not None:
                     if new_time_i <= machines[assigned_jobs[j]] and new_time_j <= machines[assigned_jobs[i]]:
                        machines[assigned_jobs[i]] -= u[job_index]
                        machines[assigned_jobs[j]] -= u[j]
                        machines[assigned_jobs[i]] += u[j]
                        machines[assigned_jobs[j]] += u[job_index]
                        assigned_jobs[i], assigned_jobs[j] = assigned_jobs[j], assigned_jobs[i]
                        improved = True

        iterations_pairwise_swapping -= 1

    for i in range(m):
        machine_jobs = [job_index+1 for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]
        print("Машина", i + 1, "виконує роботи:", machine_jobs)

    return assigned_jobs

# Крок 11
def print_results_lpt_with_job_and_pairwise_swapping(assigned_jobs, u, t):
    max_machine_time = max([sum([t[job_index] for job_index, machine_index in enumerate(assigned_jobs) if machine_index == i]) for i in range(m)])
    average_time = sum([t[i] * u[i] for i in range(len(u))]) / sum(u)

    print("Загальний час роботи бригад (в годинах):", max_machine_time)
    print("Середній час перебування громадян без світла при виконанні LPT алгоритму з попарними перестановками робіт та перестановкою робіт з однієї машини на іншу:", average_time)


# Виклик функцій
m, n, u, t = input_data()
weights = calculate_weight(u, t)
sorted_weights = sort_weights(weights)

print("LPT алгоритм:")
assigned_jobs = execute_lpt(sorted_weights, m, n, u, t)
print_results_lpt(assigned_jobs, u, t)

print("\nLPT Алгоритм з переставлянням робіт:")
assigned_jobs_with_job_swapping = execute_lpt_with_job_swapping(sorted_weights, m, n, u, t)
print_results_lpt_with_job_swapping(assigned_jobs_with_job_swapping, u, t)

print("\nLPT Алгоритм з попарним переставлянням робіт:")
assigned_jobs_with_pairwise_swapping = execute_lpt_with_pairwise_swapping(sorted_weights, m, n, u, t)
print_results_lpt_with_pairwise_swapping(assigned_jobs_with_pairwise_swapping, u, t)

print("\nLPT Алгоритм з переставлянням робіт і попарним переставлянням робіт:")
assigned_jobs_with_job_and_pairwise_swapping = execute_lpt_with_job_and_pairwise_swapping(sorted_weights, m, n, u, t)
print_results_lpt_with_job_and_pairwise_swapping(assigned_jobs_with_job_and_pairwise_swapping, u, t)

input() #wait for user input before exiting

