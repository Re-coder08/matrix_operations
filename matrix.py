import random
import numpy as np

class matrix:
    def __init__(self, rows, cols, option):
        self.rows = rows
        self.cols = cols
        self.option = option

    def create_matrix(self):
        new_matrix = []
        for i in range(self.rows):
            r = []
            for j in range(self.cols):
                if self.option == "zeros":
                    r.append(0)
                elif self.option == "random":
                    r.append(random.randint(0, 10))
                else:
                    r.append(random.randint(0, 10))

            new_matrix.append(r)

        return new_matrix

    def add(self, input, value):
        for i in range(len(input)):
            for j in range(len(input[i])):
                if isinstance(value, list):
                    input[i][j] += value[i][j]
                else:
                    input[i][j] += value

        return input

def multiply(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    print("a : "+ str(a))
    print("b : "+ str(b))
    b_transpose = matrix_transpose(b)
    print(str(b_transpose))
    result = mult(a, b, b_transpose)
    return result


def mult(a, b, b_t):
    a_dets = [len(a), len(a[0])]
    b_dets = [len(b), len(b[0])]
    print("a_dets : " + str(a_dets) + " b_dets : " + str(b_dets))
    f_dets = [a_dets[0], b_dets[1]]
    print("f_dets : " + str(f_dets))
    final_matrix = []
    for i in a:
        temp = []
        for j in b_t:
            temp.append(np.dot(i,j))
        final_matrix.append(temp)

    print("final_matrix : " + str(final_matrix))
    return final_matrix


def matrix_transpose(n):
    result = []
    for i in range(len(n[0])):
        result.append(n[:,i])

    return result


m1 = matrix(2, 2, "random")
m2 = matrix(2, 2, "random")
m1 = m1.create_matrix()
m2 = m2.create_matrix()
result = multiply(m1, m2)
print(result)
