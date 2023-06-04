# Задача 3. Создайте двумерный массив случайного размера. 
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np

# Создаем двумерный массив случайного размера
random_array = np.random.randint(0, 10, size=(np.random.randint(3, 7), np.random.randint(3, 7)))
print('\nИсходная матрица:')
print(random_array)
# Находим индексы максимального и минимального элементов
max_index = np.unravel_index(np.argmax(random_array), random_array.shape)
min_index = np.unravel_index(np.argmin(random_array), random_array.shape)
print(f'\nИндекс МАКСсимального элемента = {max_index}')
print(f'Индекс МИНимального элемента = {min_index}\n')
# Выводим элементы главной диагонали
diagonal_elements = np.diag(random_array)
print(f'Элемены главной диагонали: {diagonal_elements}')