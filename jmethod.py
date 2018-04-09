from aux import *


def jmethod(matrixA, matrixX=None, tol=1e-8):
    '''Retorna uma lista contendo uma matriz A com autovalores na diagonal e
    uma matriz X com os autovetores correspondentes'''

    # Se a matriz A nao for simetrica
    if not isSymmetric(matrixA):
        raise Exception('Matriz A deve ser simetrica.')

    # Inicia matriz X como identidade
    matrixX = np.identity(len(matrixA))

    return
