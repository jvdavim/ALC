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
    '''Dada uma matriz LU e um vetor B, retorna o vetor solucao x do sistema de equacoes lineares correspondente'''
    matrixU = np.triu(matrixLU)
    matrixL = np.tril(matrixLU)
    vectorY = np.zeros((len(matrixU), 1))
    vectorx = np.zeros((len(matrixU), 1))
    for i in range(len(matrixL)):
        matrixL[i, i] = 1.0

    # Substituicao para frente
    vectorY[0, 0] = vectorb[0, 0] / matrixL[0, 0]
    for i in range(1, len(vectorY)):
        firstSum = 0.0
        for j in range(i):
            firstSum += matrixL[i, j] * vectorY[j]
        vectorY[i, 0] = (vectorb[i, 0] - firstSum) / matrixL[i, i]

    # Substituicao para tras
    vectorx[len(vectorx)-1, 0] = vectorY[len(vectorx)-1, 0] / \
        matrixU[len(vectorx)-1, len(vectorx)-1]
    for i in range(len(vectorx)-2, -1, -1):
        secondSum = 0.0
        for j in range(i+1, len(vectorx)):
            secondSum += matrixU[i, j] * vectorx[j, 0]
        vectorx[i, 0] = (vectorY[i, 0] - secondSum) / matrixU[i, i]

    return vectorx


def biggerElementIndex(array):
    '''Retorna o indice do maior elemento do array'''
    orderedArray = np.copy(array)
    orderedArray.sort()
    return array.index(orderedArray[-1])
