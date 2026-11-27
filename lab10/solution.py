import numpy as np

def make_table(rows: int, columns: int) -> list[list[int]]:
    table = np.arange(rows * columns).reshape(rows, columns)
    return table.tolist()

def rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int) -> list[list[float]]:
    arr = np.array(matrix)
    sliced = arr[row_start:row_stop, column_start:column_stop]
    return sliced.tolist()

def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int, value: float) -> list[list[float]]:
    arr = np.array(matrix).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()

def matrix_vector_product(matrix: list[list[float]], vector: list[float]) -> list[float]:
    arr_mat = np.array(matrix)
    arr_vec = np.array(vector)
    result = arr_mat @ arr_vec
    return result.tolist()

