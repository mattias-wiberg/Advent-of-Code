with open('input.txt') as f:
    lines = f.readlines()

import numpy as np
matrix = np.array(list(map(lambda a: list(map(int,list(a))),map(lambda x: x.replace('\n',''), lines))))
gamma_list = list(map(int, np.sum(matrix, 0)>len(lines)/2))
gamma = int(''.join(map(str, gamma_list)),2)
epsilon_list = list(map(int, np.sum(matrix, 0)<len(lines)/2))
epsilon = int(''.join(map(str, epsilon_list)),2)
print(gamma*epsilon)
