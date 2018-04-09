from aux import np, isSquare


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
a = np.array([[1, 2, 2], [4, 4, 2], [4, 6, 4]])
print("\n matriz de input:\n" + str(a) + "\n")

# decomposicao lu
print("\n resultado da decomposicao LU:\n" + str(lu(a)) + "\n\n")
