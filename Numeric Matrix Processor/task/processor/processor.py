import numpy as np


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []

    def create_matrix(self):
        for i in range(self.row):
            numbers = list(map(float, input().split()))
            self.matrix.append(numbers)

    @staticmethod
    def matrix_addition(matrix1, matrix2):
        if matrix1.row == matrix2.row and matrix1.column == matrix2.column:
            result = [[matrix1.matrix[i][j] + matrix2.matrix[i][j] for j in range(len(matrix1.matrix[0]))] for i in
                      range(len(matrix1.matrix))]
            for i in result:
                i = " ".join(map(str, i))
                print(i)
        else:
            print("The operation cannot be performed")

    def multiply_by_const(self, x):
        result = []
        for i in self.matrix:
            result = [[x * self.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        for i in result:
            i = " ".join(map(str, i))
            print(i)

    @staticmethod
    def multiplication(matrix1, matrix2):
        result = [[0 for col in range(len(matrix2.matrix[0]))] for row in range(len(matrix1.matrix))]
        if matrix1.column == matrix2.row:
            for i in range(len(matrix1.matrix)):
                for j in range(len(matrix2.matrix[0])):
                    for k in range(len(matrix2.matrix)):
                        result[i][j] += matrix1.matrix[i][k] * matrix2.matrix[k][j]
        for i in result:
            i = " ".join(map(str, i))
            print(i)
        else:
            print("The operation cannot be performed")

    def transpose(self, x):
        if x == 1:
            result = [[self.matrix[j][i] for j in range(len(self.matrix))]
                      for i in range(len(self.matrix[0]))]
            for i in result:
                i = " ".join(map(str, i))
                print(i)
        if x == 2:
            result = [[self.matrix[j][i] for j in reversed(range(len(self.matrix)))]
                      for i in reversed(range(len(self.matrix[0])))]
            for i in result:
                i = " ".join(map(str, i))
                print(i)
        if x == 3:
            for i in range(len(self.matrix)):
                self.matrix[i].reverse()
            for i in self.matrix:
                i = " ".join(map(str, i))
                print(i)
        if x == 4:
            j = 0
            new_matrix = []
            for i in reversed(range(len(self.matrix))):
                new_matrix.append(self.matrix[i])
                j += 1
            for i in new_matrix:
                i = " ".join(map(str, i))
                print(i)

    def calculate_determinant(self):
        a = np.array(self.matrix)
        print(np.linalg.det(a))

    def inverse_matrix(self):
        a = np.array(self.matrix)
        if np.linalg.det(a) != 0:
            print('The result is: ')
            for i in np.linalg.inv(a):
                i = " ".join(map(str, i))
                print(i)
        else:
            print('This matrix doesn\'t have an inverse.')


def menu():
    print("""1. Add matrices
        2. Multiply matrix by a constant
        3. Multiply matrices
        4. Transpose matrix
        5. Calculate a determinant
        6. Inverse matrix
        0. Exit""")


def menu_transpose():
    print("""1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line""")


while True:
    print()
    menu()
    choice = int(input('Your choice: '))
    if choice == 1:
        n1, m1 = map(int, input('Enter size of first matrix: ').split())
        A = Matrix(n1, m1)
        print('Enter first matrix: ')
        A.create_matrix()
        n2, m2 = map(int, input('Enter size of second matrix: ').split())
        B = Matrix(n2, m2)
        print('Enter second matrix: ')
        B.create_matrix()
        print('The result is: ')
        Matrix.matrix_addition(A, B)
    if choice == 2:
        n1, m1 = map(int, input('Enter size of matrix: ').split())
        A = Matrix(n1, m1)
        print('Enter matrix: ')
        A.create_matrix()
        constant = float(input('Enter constant: '))
        print('The result is: ')
        A.multiply_by_const(constant)
    if choice == 3:
        n1, m1 = map(int, input('Enter size of first matrix: ').split())
        A = Matrix(n1, m1)
        print('Enter first matrix: ')
        A.create_matrix()
        n2, m2 = map(int, input('Enter size of second matrix: ').split())
        B = Matrix(n2, m2)
        print('Enter second matrix: ')
        B.create_matrix()
        print('The result is: ')
        Matrix.multiplication(A, B)
    if choice == 4:
        menu_transpose()
        transpose_choice = int(input('Your choice: '))
        n1, m1 = map(int, input('Enter matrix size: ').split())
        A = Matrix(n1, m1)
        print('Enter matrix: ')
        A.create_matrix()
        print('The result is: ')
        A.transpose(transpose_choice)
    if choice == 5:
        n1, m1 = map(int, input('Enter matrix size: ').split())
        A = Matrix(n1, m1)
        print('Enter matrix: ')
        A.create_matrix()
        print('The result is: ')
        A.calculate_determinant()
    if choice == 6:
        n1, m1 = map(int, input('Enter matrix size: ').split())
        A = Matrix(n1, m1)
        print('Enter matrix: ')
        A.create_matrix()
        A.inverse_matrix()
    if choice == 0:
        break

