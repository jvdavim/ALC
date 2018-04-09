import numpy as np


def pmethod(matrixA, vectorx=None, res=1):
    '''Retorna o maior autovalor do problema e seu respectivo auto vetor'''

    # Verifica se o arguento x0 foi passado e preenche com zero caso vazio
    if vectorx is None:
        vectorx = np.zeros(len(matrixA[0]))

    # Troca o tipo da matriz A e do vetor x para float
    matrixA = matrixA.astype(float)
    vectorx = vectorx.astype(float)

    # Inicia uma lista para resultado, sobrescreve o primeiro elemento de x0 com o valor 1 e inicia o autovalor como 1
    result = []
    vectorx[0] = 1.0
    lbd = 1.0

    # Enquanto residuo > tolerancia
    while res > 10**(-3):
        # Y = Ax
        vectory = np.dot(matrixA, vectorx)
        # Atualiza autovalor antigo
        plbd = lbd
        # Atualiza autovalor atual
        lbd = vectory[0]

        # Atualiza autovetor x
        for i in range(len(vectory)):
            vectorx[i] = vectory[i]/lbd

        # Computa residuo
        res = abs(lbd - plbd) / abs(lbd)

    result += [lbd, vectorx]

    return result


# ------------------------------------- main ------------------------------------- #


# inputs
a = np.array([[1.0, 0.2, 0.0], [0.2, 1.0, 0.5], [0.0, 0.5, 1.0]])
x0 = np.array([1.0, 1.0, 1.0])
print("\n matriz de input:\n" + str(a) + "\n")
print("\n vetor de input:\n" + str(x0) + "\n")

# power method
print("\n [maior autovalor, autovetor correspondente] = " + str(pmethod(a, x0)) + "\n\n")
