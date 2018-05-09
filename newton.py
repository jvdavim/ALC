from aux import np


def newtonOrig(x0=0, tol=10e-4):
    tolk = 1
    px = x0
    while (tolk > tol):
        x = px - f(px) / fl(px)
        tolk = abs(x - px)
        px = x
    return x


def newtonSec(x0=0, tol=10e-4):
    tolk = 1
    Dx = 0.001
    px = x0
    x = x0 + Dx
    fa = f(x0)
    while tolk > tol:
        fi = f(x)
        nx = x - fi*(x - px) / (fi - fa)
        tolk = abs(nx - x)
        px = x
        x = nx
        fa = fi
    return x


# ------------------------------------- main ------------------------------------- #

# inputs
def f(x):
    return x**2 - 4*np.cos(x)
def fl(x):
    return 2*x + 4*np.sin(x)
x0 = 10
tol = 5*10e-4

# newton original
x = newtonOrig(x0, tol)
print ("\nRaiz da funcao f(x) por Newton Original:\n" + str(x) + "\n")

# newton secante
x = newtonSec(x0, tol)
print ("\nRaiz da funcao f(x) por Newton Secante:\n" + str(x) + "\n")