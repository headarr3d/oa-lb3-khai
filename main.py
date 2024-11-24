from functions import Power_of5, matrix_task


def task1():
# Взаємодія зі завданням 1
    in_data = []
    print("Введіть 5 чисел для обчислення їхніх третіх ступенів:")
    for _ in range(5):
        num = float(input("Число: "))
        in_data.append(num)

    out_data = Power_of5(in_data)
    print("Числа, піднесені до кубу:", out_data)


def main():
# Меню для вибору завдання
    while True:
        print("\nОберіть завдання:")
        print("1. Обчислення третьої ступені чисел (Завдання 1)")
        print("2. Обробка матриці (Завдання 2)")
        print("3. Вихід")

        choice = input("Ваш вибір: ")
        if choice == "1":
            task1()
        elif choice == "2":
            matrix_task()
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
