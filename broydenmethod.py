from aux import np, solveLinear
from lu import lu


def broydenmethod(x0, B0, tol=10e-10, NITER=10):
    tolk = 1
    vectorpx = x0
    matrixB = B0
    count = 0
    while (tolk > tol) and (count <= NITER):
        vectorF = np.array([[f1(vectorpx)], [f2(vectorpx)]])
        vectorDx = solveLinear(lu(matrixB), np.dot(-1, vectorF))
        vectorx = vectorpx + vectorDx
        vectorY = np.array([[f1(vectorx)], [f2(vectorx)]]) - vectorF
        tolk = np.linalg.norm(vectorDx) / np.linalg.norm(vectorx)
        vectorpx = vectorx
        matrixB = matrixB + np.dot(vectorY - np.dot(matrixB, vectorDx), vectorDx.T) / np.dot(vectorDx.T, vectorDx)
        count += 1
    return vectorx


# ------------------------------------- main ------------------------------------- #

# inputs
x0 = np.array([[2], [3]])
B0 = np.array([[1,2], [4,24]])
def f1(x):
    return x[0, 0] + 2*x[1, 0] - 2
def f2(x):
    return (x[0, 0])**2 + 4*(x[1, 0])**2 - 4

# metodo de newton
x = broydenmethod(x0, B0)
print ("\nResultado do sistema pelo metodo de Broyden:\n" + str(x) + "\n")