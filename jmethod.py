from aux import *


def jmethod(matrixA, tol=1e-8):
    '''Retorna uma lista contendo uma matriz A com autovalores na diagonal e
    uma matriz X com os autovetores correspondentes'''

    # Se a matriz A nao for simetrica
    if (not isSymmetric(matrixA)) and (not isSquare(matrixA)):
        raise Exception('Matriz A deve ser simetrica.')

    # Inicia matriz X como identidade
    matrixX = np.identity(len(matrixA))

    # Inicia variavel que armazena maior valor da matriz fora da diagonal e computa primeiro valor
    maxValue = 0.0
    for i in range(len(matrixA)):
        for j in range(len(matrixA)):
            if i != j:
                if matrixA[i, j] > maxValue:
                    maxValue = abs(matrixA[i, j])
                    # Armazena o indice i (row) e o indice j (col) do maior valor
                    row = i
                    col = j

    while maxValue > tol:
        # Inicia matriz P como identidade com a mesma dimensao da matriz A
        matrixP = np.identity(len(matrixA))

        # Reseta o valor maximo
        maxValue = 0.0

        # Computa fi
        if matrixA[row, row] != matrixA[col, col]:
            fi = (1.0 / 2.0) * \
                (np.arctan((2.0 * matrixA[row, col]) /
                           (matrixA[row, row] - matrixA[col, col])))

        elif matrixA[row, row] == matrixA[col, col]:
            fi = np.pi/4.0

        else:
            raise Exception(
                'A[i][i] != A[j][j] e A[i][i] == A[j][j] sao falsos ao mesmo tempo.')

        # Computa matriz P
        matrixP[row, row] = np.cos(fi)
        matrixP[row, col] = -np.sin(fi)
        matrixP[col, row] = np.sin(fi)
        matrixP[col, col] = np.cos(fi)

        # Atualiza matriz A e matriz X
        matrixA = np.dot(matrixP.T, np.dot(matrixA, matrixP))
        matrixX = np.dot(matrixX, matrixP)

        # Atualiza o mairo valor da matriz fora da diagonal e seus indices
        for i in range(len(matrixA)):
            for j in range(len(matrixA)):
                if i != j:
                    if abs(matrixA[i, j]) >= maxValue:
                        maxValue = abs(matrixA[i, j])
                        # Armazena o indice i (row) e o indice j (col) do maior valor
                        row = i
                        col = j

    # Atualiza os elementos fora da diagonal como zero para ficar mais legivel
    for i in range(len(matrixA)):
        for j in range(len(matrixA)):
            if i != j:
                matrixA[i][j] = 0.0

    return [matrixA, matrixX]


# ------------------------------------- main ------------------------------------- #


# inputs
a = np.array([[1.0, 0.2, 0.0], [0.2, 1.0, 0.5], [0.0, 0.5, 1.0]])
print("\nmatriz de input A:\n" + str(a))

# metodo de jacobi para autovalor/autovetor
result = jmethod(a)
print("\nmatriz de autovalores A:\n" +
      str(result[0]) + "\n\nmatriz de autovetores X:\n" + str(result[1]) + "\n\n")
