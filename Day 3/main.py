with open('input.txt') as f:
    lines = f.readlines()

import numpy as np
matrix = np.array(list(map(lambda a: list(map(int, list(a))),
                  map(lambda x: x.replace('\n', ''), lines))))
gamma_list = list(map(int, np.sum(matrix, 0) > len(lines)/2))
gamma = int(''.join(map(str, gamma_list)), 2)
epsilon_list = list(map(int, np.sum(matrix, 0) < len(lines)/2))
epsilon = int(''.join(map(str, epsilon_list)), 2)
print(gamma*epsilon)


def fun(matrix, ret, mode):
    col_sum = np.sum(matrix[:, 0])
    if matrix.shape[1] != 1 and matrix.shape[0] != 1:
        if col_sum < len(matrix[:, 0])/2:  # More zeros
            return fun(matrix[matrix[:, 0] == np.abs(0+mode), 1:], ret + str(np.abs(0+mode)), mode)
        else:  # More ones or equal
            return fun(matrix[matrix[:, 0] == np.abs(0+mode), 1:], ret + str(np.abs(1+mode)), mode)
    else:  # last bit
        if col_sum < len(matrix[:, 0])/2:  # More zeros
            return ret + str(np.abs(0+mode))
        else:  # More ones or equal
            return ret + str(np.abs(1+mode))


oxygen = fun(matrix, "", 0)
co2 = fun(matrix, "", -1)
print(int(oxygen, 2)*int(co2, 2))
