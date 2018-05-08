from aux import np, isSquare, solveLinear


def lu(matrixA):
    '''Decomposicao LU da matriz matrixA. Retorna matriz LU concatenada.'''
    # Inicia matriz LU como uma copia da matriz A
    matrixLU = matrixA.astype(float)

    # Verifica se matriz LU e quadrada
    if not isSquare(matrixLU):
        raise IndexError('A matriz inserida deve ser quadrada.')

    # Computa os elementos da matriz LU
    for k in range(len(matrixLU)):
        for i in range(k + 1, len(matrixLU)):
            matrixLU[i, k] = matrixLU[i][k] / matrixLU[k][k]

        for j in range(k + 1, len(matrixLU)):
            for i in range(k + 1, len(matrixLU)):
                matrixLU[i, j] = matrixLU[i, j] - \
                    (matrixLU[i, k] * matrixLU[k, j])

    return matrixLU


# ------------------------------------- main ------------------------------------- #



# inputs
a = np.array([[4.5, 2.5, 1.5, 0.5, 1.0, 0.5], [2.5, 5.0, 2.5,
                                               1.5, 0.5, 1.0], [1.5, 2.5, 4.5, 2.5, 0.5, 1.0], [0.5, 1.5, 2.5, 3.0, 0.5, 1.0], [1.0, 0.5, 0.5, 0.5, 2.5, 1.5], [0.5, 1.0, 1.0, 1.0, 1.5, 2.0]])
print("\nmatriz de input A:\n" + str(a) + "\n")
b = np.array([10.0, 20.0, 30.0, 40.0, 30.0, 10.0])
print("\nmatriz de input b:\n" + str(b) + "\n")

# decomposicao lu
LU = lu(a)
print("\nresultado da decomposicao LU:\n" + str(LU) + "\n")

# Resultado de Ax = b
x = solveLinear(LU, b)
# print("\nvetor resultado x:\n" + str(x) + "\n")
# print("\nmultiplicacao Ax (tem que ser igual a b):\n" + str(np.dot(a, x)) + "\n")
