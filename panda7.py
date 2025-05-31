import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных по 5 элементов каждый
array1 = np.random.rand(5)
array2 = np.random.rand(5)

print("Array 1:", array1)
print("Array 2:", array2)

# Построение диаграммы рассеяния
plt.scatter(array1, array2)
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.xlabel('Массив 1')
plt.ylabel('Массив 2')
plt.show()