from aux  import np


def bissecao(a, b, tol=10e-3):
    '''Dado um intervalo [a,b] e uma tolerancia tol, retorna a raiz da funcao f(x)'''
    c = 0
    while (abs(b - a) > tol):
        xi = (a + b) / 2.0
        fi = f(xi)
        if (f(a) < 0) and (f(b) > 0):
            if fi > 0.0:
                b = xi
            else:
                a = xi
        elif (f(a) > 0) and (f(b) < 0):
            if fi > 0.0:
                a = xi
            else:
                b = xi
        c += 1
    print(c)
    return xi


# ------------------------------------- main ------------------------------------- #


# inputs
def f(x):
    return np.exp(-x) - x/2
a = 0.5
b = 2.0
tol = 10e-7

# bissecao
x = bissecao(a, b, tol)
print ("\nRaiz da funcao f(x):\n" + str(x) + "\n")