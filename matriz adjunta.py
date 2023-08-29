import sympy as sp

# Defina a variável simbólica
S = sp.symbols('S')

# Defina a matriz 3x3 com variáveis
A = sp.Matrix([[S-3, 5, -2],
               [-1, S+8, -7],
               [3, 6, S-2]])

# Função para calcular o cofator de um elemento (i, j)
def cofactor(matrix, i, j):
    submatrix = matrix.copy()
    submatrix.row_del(i)
    submatrix.col_del(j)
    return (-1) ** (i + j) * submatrix.det()

# Calcula a matriz adjunta
adjoint = sp.Matrix.zeros(3, 3)
for i in range(3):
    for j in range(3):
        adjoint[i, j] = cofactor(A, i, j)  # Transposta dos cofatores

print("Matriz Adjunta:")
print(adjoint)