import lu
from aux  import np


def bissecao(a, b, tol=10e-8):
    while (abs(b - a) > tol):
        xi = (a + b) / 2.0
        fi = f(xi)
        if fi > 0.0:
            b = xi
        else:
            a = xi
    return xi


# ------------------------------------- main ------------------------------------- #


# inputs
def f(x):
    return x**2 - 4*np.cos(x)
a = 0
b = 10
tol = 10e-4

# bissecao
x = bissecao(a, b, tol)
print ("\nRaiz da funcao f(x):\n" + str(x) + "\n")