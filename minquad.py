import numpy as np


def minquad(points=np.array([[0, 0], [1, 1]])):

    for p in points:
        if len(p) != 2:
            raise Exception(
                'Cada elemento do vetor do array de input deve ser um array de 2 elementos')

    # Inicia a matriz P e computa seus respectivos elementos
    matrixP = np.zeros((len(points), 2))
    for p in range(len(points)):
        # Primeira coluna = 1
        matrixP[p, 0] = 1
        # Segunda coluna = vetor das cordenadas x passadas no argumento
        matrixP[p, 1] = points[p, 0]

    # Inicia a vetor Y e computa seus respectivos elementos
    vectorY = np.zeros(len(points))
    for p in range(len(points)):
        # Vetor das coordenadas y passadas no argumento
        vectorY[p] = points[p, 1]

    matrixA = np.dot(matrixP.T, matrixP)
    matrixC = np.dot(matrixP.T, vectorY)
    vectorB = np.dot(np.linalg.inv(matrixA), matrixC)

    return [vectorB[0], vectorB[1]]


# ------------------------------------- main ------------------------------------- #


# inputs
p = np.array([[1.0, 2.0], [2.0, 3.5], [3.0, 6.5]])
print("\nLista de pontos de input:\n" + str(p))

# metodo dos minimos quadrados
B = minquad(p)
print("\nCoeficientes encontrados:\n" + "a = " + str(B[1]) + "  e  b = " + str(B[0]))
