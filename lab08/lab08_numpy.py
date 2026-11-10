import numpy as np

hours = np.arange(0, 22, 3)
print('hours:', hours)
print('shape:', hours.shape, 'ndim:', hours.ndim, 'size:', hourse.size, 'dtype:', hours.dtype)

line = np.linspace(0, 1, 5)
print('line:', line)

zeros = np.zeros(dtype=int)
print('zeros:', zeros)

unknown_table = np.full((2, 3), -1)
print('unknown_table:', unknown_table)

identity = np.eye(3)
print('identity:', identity)


print('3 элемент:', hours[2])
print('последний элемент:', hours[-1])
print('с индексами 2-5:', hours[2:6])
print('каждый второй элемент:', hours[::2])
print('в обратном порядке:', hours[::-1])


temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print('форма:', temperatures.shape)
print('число измерений:', temperatures.ndim)
print('число элементов:', temperatures.size)
print('значение из 2 строки и 3 столбца:', temperatures[1, 2])
print('первая строка:', temperatures[0])
print('последний столбец:', temperatures[:, -1])
print('первые две строки без первого столбца:', temperatures[:2, 1:])
print('центральный фрагмент:', temperatures[:2, 1:3])


matrix = np.arange(1, 26).reshape(5, 5)

first_three = matrix[:3]
print('первые три строки:', first_three, 'shape:', first_three.shape)

last_two = matrix[-2:]
print('последние две строки:', last_two, 'shape:', last_two.shape)

first_two_cols = matrix[:, :2]
print('первые два столбца:', first_two_cols, 'shape:', first_two_cols.shape)

fragment = matrix[1:4, 2:5]
print('фрагмент из строк 1-3 и столбцов 2-4:', fragment, 'shape:', fragment.shape)

corner = matrix[-2:, -2:]
print('угловой блок 2 на 2:', corner, 'shape:', corner.shape)


vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print('changed_hours:', changed_hours)
print('исходный hours:', hours)
# если написать changed_hours = hours, то в Python переменная changed_hours не создаст новый массив, а просто станет ссылкой на тот же участок памяти, где лежит hours, те любое изменение в changed_hours изменит и hours, copy() создает физическую копию массива в памяти

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print('итоговая changed_matrix:', changed_matrix)
print('исходная matrix:', matrix)


numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print('форма numbers:', numbers.shape)
print('форма table:', table.shape)
print('форма transposed:', transposed.shape)
# reshape(3, 4) работает тк 3 * 4 = 12 и все элементы помещаются, а reshape(5, 3) вызовет ошибку тк 5 * 3 = 15 и нам не хватит 3 элемента
