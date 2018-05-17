from aux import np, solveLinear
from lu import lu


def newtonmethod(x0, tol=10e-7):
    tolk = 1
    vectorpx = x0

    while tolk>tol:
        matrixJ = Jacob(vectorpx)
        vectorF = np.array([[f1(vectorpx)], [f2(vectorpx)]])
        vectorDx = solveLinear(lu(matrixJ), np.dot(-1, vectorF))
        vectorx = vectorpx + vectorDx
        tolk = np.linalg.norm(vectorDx) / np.linalg.norm(vectorx)
        vectorpx = vectorx

    return vectorx


# ------------------------------------- main ------------------------------------- #

# inputs
x0 = np.array([[2], [3]])
def f1(x):
    return x[0, 0] + 2*x[1, 0] - 2
def f2(x):
    return (x[0, 0])**2 + 4*(x[1, 0])**2 - 4

def Jacob(x):
    return np.array([[1, 2], [2*x[0, 0], 8*x[1, 0]]])

# metodo de newton
x = newtonmethod(x0)
print ("\nResultado do sistema pelo metodo de Newton:\n" + str(x) + "\n")