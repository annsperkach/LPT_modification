import random
 
# Крок 1 - Введемо дані для роботи з алгоритмами
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
