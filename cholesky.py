from aux import *


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
a = np.array([[1, 0.2, 0.4], [0.2, 1, 0.5], [0.4, 0.5, 1]])
print("\n matriz de input:\n" + str(a) + "\n")

# decomposicao de cholesky
print("\n resultado da decomposicao de Cholesky:\n" + str(cholesky(a)) + "\n\n")
