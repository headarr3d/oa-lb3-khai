import numpy as np


# Завдання 1. Функція PowerA3
def PowerA3(A):
    return A ** 3


def Power_of5(in_lst):
    return [PowerA3(A) for A in in_lst]


# Завдання 2. Функції для роботи з матрицею
def process_matrix(filename, K):
    # Читаємо матрицю з файлу
    matrix = np.loadtxt(filename, dtype=float)

    # Перевірка коректності K
    if K < 1 or K > matrix.shape[0]:
        raise ValueError("K повинен бути в межах 1 ≤ K ≤ M")

    # Обчислення параметрів K-го рядка
    row = matrix[K - 1]  # K-й рядок (нумерація з 0)
    row_sum = np.sum(row)
    row_product = np.prod(row)

    # Обчислення різниці матриці з одиничною
    identity_matrix = np.eye(matrix.shape[0], matrix.shape[1])
    matrix_diff = matrix - identity_matrix

    return row_sum, row_product, matrix_diff


def matrix_task():
    filename = input("Введіть ім'я файлу з матрицею: ")
    K = int(input("Введіть номер рядка K (1 ≤ K ≤ M): "))
    try:
        row_sum, row_product, matrix_diff = process_matrix(filename, K)
        print(f"Сума елементів K-го рядка: {row_sum}")
        print(f"Добуток елементів K-го рядка: {row_product}")
        print("Різниця матриці з одиничною матрицею:")
        print(matrix_diff)
    except Exception as e:
        print(f"Помилка: {e}")
