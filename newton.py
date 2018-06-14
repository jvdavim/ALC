from aux import np


def newtonOrig(x0=0, tol=10e-4, NITER=10):
    '''Dado um ponto inicial x0 e uma tolerancia tol, retorna a raiz da funcao f(x)'''
    tolk = 1
    px = x0
    count = 0
    while (tolk > tol) and (count <= NITER):
        x = px - f(px) / fl(px)
        tolk = abs(x - px)
        px = x
        count += 1
    print(count)
    return x


def newtonSec(x0=0, tol=10e-4, NITER=10):
    '''Dado um ponto inicial x0 e uma tolerancia tol, retorna a raiz da funcao f(x)'''    
    tolk = 1
    Dx = 0.001
    px = x0
    x = x0 + Dx
    fa = f(x0)
    count = 0
    while (tolk > tol) and (count <= NITER):
        fi = f(x)
        nx = x - fi*(x - px) / (fi - fa)
        tolk = abs(nx - x)
        px = x
        x = nx
        fa = fi
        count += 1
    print(count)
    return x


# ------------------------------------- main ------------------------------------- #

# inputs
def f(x):
    return np.exp(-x) - x/2
def fl(x):
    return -np.exp(-x) - 1/2
x0 = 10
tol = 10e-3

# newton original
x = newtonOrig(x0, tol)
print ("\nRaiz da funcao f(x) por Newton Original:\n" + str(x) + "\n")

# newton secante
x = newtonSec(x0, tol)
print ("\nRaiz da funcao f(x) por Newton Secante:\n" + str(x) + "\n")