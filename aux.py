import numpy as np


def isSymmetric(matrixA, tol=1e-8):
    return np.allclose(matrixA, matrixA.T, atol=tol)

def isSquare(matrixA):
    '''Retorna True caso a matriz A seja quadrada e False caso contrario'''
    if matrixA.shape[0] == matrixA.shape[1]:
        return True
    return False