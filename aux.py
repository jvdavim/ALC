import numpy as np
import math


def isDiagonallyDominant(matrixA):
    '''Retorna True caso a matriz A seja diagonal dominante e False caso contrario'''
    for i in range(len(matrixA)):
        sum1 = 0.0
        sum2 = 0.0
        for j in range(len(matrixA)):
            if i != j:
                sum1 += abs(matrixA[i, j])
                sum2 += abs(matrixA[j, i])
        if (abs(matrixA[i, i]) < sum1) or (abs(matrixA[i, i] < sum2)):
            return False
    return True


def isSquare(matrixA):
    '''Retorna True caso a matriz A seja quadrada e False caso contrario'''
    if matrixA.shape[0] == matrixA.shape[1]:
        return True
    return False


def solveLinear(matrixLU, vectorb):
    matrixU = np.triu(matrixLU)
    matrixL = np.tril(matrixLU)
    vectorY = np.zeros(len(matrixU))
    vectorx = np.zeros(len(matrixU))
    for i in range(len(matrixL)):
        matrixL[i, i] = 1.0

    # Substituicao para frente
    vectorY[0] = vectorb[0] / matrixL[0, 0]
    for i in range(1, len(vectorY)):
        firstSum = 0.0
        for j in range(i):
            firstSum += matrixL[i, j] * vectorY[j]
        vectorY[i] = (vectorb[i] - firstSum) / matrixL[i, i]
    print("\nVector Y:\n" + str(vectorY) + "\n")

    # Substituicao para tras
    vectorx[len(vectorx)-1] = vectorY[len(vectorx)-1] / matrixU[len(vectorx)-1, len(vectorx)-1]
    for i in range(len(vectorx)-2, -1, -1):
        secondSum = 0.0
        for j in range(i+1, len(vectorx)):
            secondSum += matrixU[i, j] * vectorx[j]
        vectorx[i] = (vectorY[i] - secondSum) / matrixU[i, i]
    print("\nVector x:\n" + str(vectorx) +"\n")
    print("\nMultiplicacao Ux (tem que ser igual a Y):\n" + str(np.dot(matrixU,vectorx)) + "\n")

    return vectorx