import matplotlib.pyplot as plt

def execution_time_plot(algorithms, execution_times):
    # Створення порівняльного графіку за часом виконання алгоритмів
    plt.bar(algorithms, execution_times)
    plt.xlabel('Алгоритм')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння часу виконання алгоритмів LPT')
    plt.show()

def diff_amount_m_plot(algorithm, execution_times):
    # Створення графіку за часом виконання алгоритму при зміні кількості машин
    machines = list(range(1, len(execution_times) + 1))
    plt.plot(machines, execution_times)
    plt.xlabel('Кількість машин')
    plt.ylabel('Час виконання (секунди)')
    plt.title(f'Залежність часу виконання алгоритму {algorithm} від кількості машин')
    plt.show()

def diff_amount_n_plot(algorithm, execution_times):
    # Створення графіку за часом виконання алгоритму при зміні кількості робіт
    jobs = list(range(1, len(execution_times) + 1))
    plt.plot(jobs, execution_times)
    plt.xlabel('Кількість робіт')
    plt.ylabel('Час виконання (секунди)')
    plt.title(f'Залежність часу виконання алгоритму {algorithm} від кількості робіт')
    plt.show()

def show_plots(algorithms, execution_times):
  option = int(input("Виберіть вид графіку для виводу: \n1 - Графік порівняння часу виконання алгоритмів LPT \n2 - Графік порівняння часу виконання алгоритмів LPT при зміні кількості машин\n3 - Графік порівняння часу виконання алгоритмів LPT при зміні кількості робіт\n"))
  if option == 1:
        execution_time_plot(algorithms, execution_times)
  elif option == 2:
        algorithm = input("Введіть назву алгоритму: ")
        diff_amount_m_plot(algorithm, execution_times)
  elif option == 3:
        algorithm = input("Введіть назву алгоритму: ")
        diff_amount_n_plot(algorithm, execution_times)
  else:
        print("Невірний вибір опції!")
        return show_plots()