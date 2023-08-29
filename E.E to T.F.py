import numpy as np
import sympy as sp

def state_space_to_transfer_function(A, B, C, D):
    s = sp.symbols('s')
    I = sp.eye(A.shape[0])
    
    M = s * I - A
    N = M.inv()
    
    transfer_function = C @ N @ B + D
    transfer_function = transfer_function[0, 0]
    
    return sp.simplify(transfer_function)

# Perguntar o tamanho da matriz
num_states = int(input("Digite o número de estados da matriz: "))
num_inputs = int(input("Digite o número de entradas da matriz: "))
num_outputs = int(input("Digite o número de saídas da matriz: "))

# Receber as matrizes de espaço de estados do usuário
A = np.zeros((num_states, num_states))
B = np.zeros((num_states, num_inputs))
C = np.zeros((num_outputs, num_states))
D = np.zeros((num_outputs, num_inputs))

for i in range(num_states):
    for j in range(num_states):
        A[i, j] = float(input(f"Digite o valor de A({i+1},{j+1}): "))

for i in range(num_states):
    for j in range(num_inputs):
        B[i, j] = float(input(f"Digite o valor de B({i+1},{j+1}): "))

for i in range(num_outputs):
    for j in range(num_states):
        C[i, j] = float(input(f"Digite o valor de C({i+1},{j+1}): "))

for i in range(num_outputs):
    for j in range(num_inputs):
        D[i, j] = float(input(f"Digite o valor de D({i+1},{j+1}): "))

transfer_function = state_space_to_transfer_function(A, B, C, D)
print("Função de Transferência:", transfer_function)