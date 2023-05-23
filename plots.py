import matplotlib.pyplot as plt

def execution_time_plot(algorithms, execution_times):
    # Створення порівняльного графіку за часом виконання алгоритмів
    plt.bar(algorithms, execution_times)
    plt.xlabel('Алгоритм')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння часу виконання алгоритмів LPT')
    plt.show()

def diff_amount_m_plot(algorithms, execution_times):
    # Створення порівняльного графіку за часом виконання алгоритмів
    plt.bar(algorithms, execution_times)
    plt.xlabel('Алгоритм')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння часу виконання алгоритмів LPT при зміні кількості машин')
    plt.show()

def diff_amount_n_plot(algorithms, execution_times):
    # Створення порівняльного графіку за часом виконання алгоритмів
    plt.bar(algorithms, execution_times)
    plt.xlabel('Алгоритм')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння часу виконання алгоритмів LPT при зміні кількості робіт')
    plt.show()

def show_plots(algorithms, execution_times):
  option = int(input("Виберіть вид графіку для виводу: \n1 - Графік порівняння часу виконання алгоритмів LPT \n2 - Графік порівняння часу виконання алгоритмів LPT при зміні кількості машин\n3 - Графік порівняння часу виконання алгоритмів LPT при зміні кількості робіт"))
  if option == 1:
        execution_time_plot(algorithms, execution_times)
  elif option == 2:
       diff_amount_m_plot(algorithms, execution_times)
  elif option == 3:
       diff_amount_n_plot(algorithms, execution_times)
  else:
        print("Невірний вибір опції!")
        return show_plots()