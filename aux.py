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
