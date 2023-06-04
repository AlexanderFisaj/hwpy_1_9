# Задача 1. Дан список элементов. Используя библиотеку NumPy, 
# подсчитайте количество уникальных элементов в нём.

from random import randint
import numpy as np


# Задаем список рандомных элементов
elements_list = [randint(1, 10) for _ in range(10)]
# визуализируем в терминале полученный список
print(elements_list)
# Используем функцию unique для уникальных элементов и их подсчета
unique_elements, counts = np.unique(elements_list, return_counts=True)

# Вывод результата
for element, count in zip(unique_elements, counts):
    print(f"Элемент {element} встречается {count} раз")