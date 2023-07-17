# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    # Определяем число строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])
    # Создаем новую матрицу с помощью списка списков
    transposed_matrix = [[0 for j in range(rows)] for i in range(cols)]
    # Проходимся по каждому элементу в матрице
    for i in range(rows):
        for j in range(cols):
            # Записываем транспонированный элемент в новую матрицу
            transposed_matrix[j][i] = matrix[i][j]
    # Возвращаем транспонированную матрицу
    return transposed_matrix


matrix_example = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
print(transpose_matrix(matrix_example))
