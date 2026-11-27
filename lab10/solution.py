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

def matrix_multiply(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    arr_left = np.array(left)
    arr_right = np.array(right)
    result = arr_left @ arr_right
    return result.tolist()

def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    arr = np.array(matrix)
    result = arr.T
    return result.tolist()

def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    arr_mat = np.array(matrix)
    arr_vec = np.array(vector)
    solution = np.linalg.solve(arr_mat, arr_vec)
    rounded = np.round(solution, 6)
    return rounded.tolist()

def tensor_channel_mean(tensor: list) -> list:
    arr = np.array(tensor)
    mean_arr = arr.mean(axis=-1)
    return mean_arr.tolist()

def point_distance(first: list[float], second: list[float]) -> float:
    arr_first = np.array(first)
    arr_second = np.array(second)
    dist = np.linalg.norm(arr_first - arr_second)
    return float(np.round(dist, 6))
