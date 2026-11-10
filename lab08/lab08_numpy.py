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

