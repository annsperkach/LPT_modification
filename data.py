import random
 
# Крок 1 - Введемо дані для роботи з алгоритмами
def input_data():
    option = int(input("Введіть опцію для введення даних (1 - статично, 2 - згенерувати рандомом, 3 - ввести дані вручну, 4 - зчитування з файлу): "))
    if option == 1:
        global m, n, u, t
        m = 3
        n = 10
        u = [53, 26, 30, 80, 24, 55, 25, 5, 90, 38]
        t = [5, 2, 3, 6, 2, 5, 2, 1, 7, 4]
    elif option == 2:
        m = int(input("Введіть кількість машин: "))
        n = int(input("Введіть кількість робіт: "))
        u = [random.randint(1, 100) for _ in range(n)]
        t = [random.randint(1, 15) for _ in range(n)]
    elif option == 3:
        m = int(input("Введіть кількість машин: "))
        n = int(input("Введіть кількість робіт: "))
        # приклад дати 
        # u = 53 25 30 80 24 55 25 5 90 38
        # t = 5 2 3 6 2 5 2 1 7 4
        u = list(map(int, input("Введіть значення u (значення відділені пробілом): ").split()))
        t = list(map(int, input("Введіть значення t (значення відділені пробілом): ").split()))
    elif option == 4:
        filename = 'data.txt'  # Назва файлу з даними
        m, n, u, t = read_data_from_file(filename)
    else:
        print("Невірний вибір опції!")
        return input_data()

    #print("m =", m)
    #print("n =", n)
    #print("u =", u)
    #print("t =", t)    
    return m, n, u, t

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Зчитуємо всі рядки з файлу
        m = int(lines[0])  # Зчитуємо перший рядок файлу як число m
        n = int(lines[1])  # Зчитуємо другий рядок файлу як число n
        u = list(map(int, lines[2].split()))  # Зчитуємо третій рядок файлу як список цілих чисел u
        t = list(map(int, lines[3].split()))  # Зчитуємо четвертий рядок файлу як список цілих чисел t
        return m, n, u, t