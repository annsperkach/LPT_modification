import matplotlib.pyplot as plt

def execution_time_plot(algorithms, execution_times):
    # Створення порівняльного графіку за часом виконання алгоритмів
    for i in range(len(algorithms)):
       plt.bar(algorithms[i], execution_times[i])
    plt.xlabel('Алгоритм')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння часу виконання алгоритмів LPT')
    plt.show()

def diff_amount_m_plot(algorithms, execution_times):
    # Створення графіку за часом виконання алгоритму при зміні кількості машин
    for i in range(len(algorithms)):
        plt.plot(execution_times[i], label=algorithms[i])  # Перемістити аргументи у правильному порядку
    plt.xlabel('Кількість машин')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Залежність часу виконання алгоритмів від кількості машин')
    plt.legend()  # Додати легенду для алгоритмів
    plt.show()

def diff_amount_n_plot(algorithms, execution_times):
    # Створення графіку за часом виконання алгоритму при зміні кількості робіт
    jobs = list(range(1, len(execution_times) + 1))
    for i in range(len(algorithms)):
        plt.plot(execution_times[i], label=algorithms[i])  # Перемістити аргументи у правильному порядку
    plt.xlabel('Кількість машин')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Залежність часу виконання алгоритмів від кількості машин')
    plt.legend()  # Додати легенду для алгоритмів
    plt.show()

def show_plots(algorithms, execution_times):
  option = int(input("Виберіть вид графіку для виводу: \n1 - Графік порівняння часу виконання алгоритмів LPT \n2 - Графік порівняння часу виконання алгоритмів LPT при зміні кількості машин\n3 - Графік порівняння часу виконання алгоритмів LPT при зміні кількості робіт\n"))
  if option == 1:
        execution_time_plot(algorithms, execution_times)
  elif option == 2:
        diff_amount_m_plot(algorithms, execution_times)
  elif option == 3:
        diff_amount_n_plot(algorithms, execution_times)
  else:
        print("Невірний вибір опції!")
        return show_plots()