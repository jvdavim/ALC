from aux import np, solveLinear
from lu import lu


def newtonmethod(x0, tol=10e-7, NITER=100):
    '''Dado um vetor inicial x0 e uma tolerancia tol, retorna o vetor solucao do sistema de equacoes nao lineares'''
    tolk = 1
    vectorpx = x0
    count = 0
    while (tolk > tol) and (count <= NITER):
        matrixJ = Jacob(vectorpx)
        vectorF = np.array([[f1(vectorpx)], [f2(vectorpx)]])
        vectorDx = solveLinear(lu(matrixJ), np.dot(-1, vectorF))
        vectorx = vectorpx + vectorDx
        tolk = np.linalg.norm(vectorDx) / np.linalg.norm(vectorx)
        vectorpx = vectorx
        count += 1
    print(count)
    return vectorx


# ------------------------------------- main ------------------------------------- #

# inputs
x0 = np.array([[1], [1]])
def f1(x):
    return x[0, 0] - x[1, 0] + 2
def f2(x):
    return np.exp(x[0, 0]) + x[1, 0] - 5

def Jacob(x):
    return np.array([[1, -1], [np.exp(x[0, 0]), 1]])

# metodo de newton
x = newtonmethod(x0)
print ("\nResultado do sistema pelo metodo de Newton:\n" + str(x) + "\n")