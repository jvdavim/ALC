from aux import np, isSquare, solveLinear, math


def cholesky(matrixA):
    '''Aplica a decomposicao de Cholesky na matriz A e retorna a matriz L'''
    # Inicia matriz L
    matrixL = (len(matrixA), len(matrixA))
    matrixL = np.zeros(matrixL)

    # Verifica se a matriz e quadrada
    if not isSquare(matrixL):
        raise Exception('A matriz deve ser quadrada')

    # Computa os elementos da matriz L
    for i in range(len(matrixL)):
        # Variavel para computar o primeiro somatorio
        firstSum = 0.0

        # Computa o primeiro somatorio
        for k in range(i):
            firstSum += matrixL[i, k] ** 2

        # Computa a diagonal da matriz L
        matrixL[i, i] = math.sqrt(matrixA[i][i] - firstSum)

        # Computa os elementos fora da diagonal da matriz L
        for j in range(i+1, len(matrixL)):
            # Variavel para computar o segundo somatorio
            secondSum = 0.0

            # Computa o segundo somatorio
            for k in range(i):
                secondSum += matrixL[i, k] * matrixL[j, k]

            # Computa elementos fora da diagonal da matriz L
            matrixL[j, i] = (1.0 / matrixL[i, i]) * \
                (matrixA[i, j] - secondSum)

    return matrixL


# ------------------------------------- main ------------------------------------- #


# inputs
a = np.array([[4.5, 2.5, 1.5, 0.5, 1.0, 0.5], [2.5, 5.0, 2.5,
                                               1.5, 0.5, 1.0], [1.5, 2.5, 4.5, 2.5, 0.5, 1.0], [0.5, 1.5, 2.5, 3.0, 0.5, 1.0], [1.0, 0.5, 0.5, 0.5, 2.5, 1.5], [0.5, 1.0, 1.0, 1.0, 1.5, 2.0]])
print("\nmatriz de input A:\n" + str(a) + "\n")
b = np.array([10.0, 20.0, 30.0, 40.0, 30.0, 10.0])
print("\nmatriz de input b:\n" + str(b) + "\n")

# decomposicao de cholesky
L = cholesky(a)
print("\n resultado da decomposicao de Cholesky:\n" + str(L) + "\n\n")

# matriz LU em cholesky pode ser descrita como LL.T
LU = np.zeros((len(L),len(L)))
for i in range(len(L)):
    for j in range(len(L)):
        LU[i, j] = L[i, j]
        LU[j, i] = L[i, j]

# resultado de Ax = b
x = solveLinear(LU, b)
print("\nvetor resultado x:\n" + str(x) + "\n")
print("\nmultiplicacao Ax (tem que ser igual a b):\n" + str(np.dot(a, x)) + "\n")