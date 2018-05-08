from aux import np


def newton(x0=0, tol=10e-4):
    tolk = 1
    px = x0
    while (tolk > tol):
        x = px - f(px) / fl(px)
        tolk = abs(x - px)
        px = x
    return x


# ------------------------------------- main ------------------------------------- #

# inputs
def f(x):
    return x**2 - 4*np.cos(x)
def fl(x):
    return 2*x + 4*np.sin(x)
x0 = 10
tol = 5*10e-4

# newton
x = newton(x0, tol)
print ("\nRaiz da funcao f(x):\n" + str(x) + "\n")