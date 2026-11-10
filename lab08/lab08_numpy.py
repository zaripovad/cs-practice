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


