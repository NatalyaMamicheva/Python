class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(["%d\t" % i for i in row]) for row in self.matrix])


    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

m1 = Matrix([[31, 22, 0], [37, 43, 0], [51, 86, 0]])
m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, 0]])
print(m1 + m2)