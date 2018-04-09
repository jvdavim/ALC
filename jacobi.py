from aux import np, isSquare, isDiagonallyDominant


def jacobi(matrixA, vectorb, vectorx=None, res=1):
    '''Resolve a equacao Ax=b pelo metodo iterativo de Jacobi.'''

    if isSquare(matrixA) and isDiagonallyDominant(matrixA):
        if vectorx is None:
            vectorx = np.zeros(len(matrixA[0]))

        # Computa a diagonal da matriz A
        matrixD = np.diag(matrixA)
        # Computa a matriz R = A - D
        matrixR = matrixA - np.diagflat(matrixD)

        # Iterar ate  residuo > tolerancia
        while res > 10**(-5):
            # Armazena vetor x da iteracao anterior
            pvectorx = np.copy(vectorx)
            # Computa vetor x da iteracao atual
            vectorx = (vectorb - np.dot(matrixR, vectorx)) / matrixD
            # Computa novo residuo
            res = np.linalg.norm(vectorx - pvectorx) / np.linalg.norm(vectorx)

    else:
        raise Exception('A matriz inserida deve ser diagonal dominante.')

    return vectorx


# ------------------------------------- main ------------------------------------- #


# inputs
a = np.array([[3, -1, -1], [-1, 3, -1], [-1, -1, 3]])
x0 = np.array([1, 1, 1])
b = np.array([1, 2, 1])
print("\n matriz de input:\n" + str(a) + "\n")

# decomposicao de jacobi
print("\n resultado da rotina Jacobi:\n" + str(jacobi(a, b, x0)) + "\n\n")
