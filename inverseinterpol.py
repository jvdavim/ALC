from aux import np, biggerElementIndex


def inverseInterpolate(x=[0,1,2], tol=10e-4, NITER=10):
    tolk = 1
    px = 10e+36
    count = 0
    while (tolk > tol) and (count <= NITER):
        y = [f(x[0]), f(x[1]), f(x[2])]
        xk = (y[1]*y[2]*x[0]) / ((y[0]-y[1])*(y[0]-y[2])) + (y[0]*y[2]*x[1]) / \
            ((y[1]-y[0])*(y[1]-y[2])) + (y[0]*y[1]*x[2]) / ((y[2]-y[0])*(y[2]-y[1]))
        tolk = abs(xk - px)
        px = xk
        biggerIndexY = biggerElementIndex(y)
        x[biggerIndexY] = xk
        y[biggerIndexY] = f(xk)
        x.sort()
        y.sort()
        count += 1
    return xk


# ------------------------------------- main ------------------------------------- #

# inputs
def f(x):
    return x**2 - 4*np.cos(x)
tol = 5*10e-7

# interpolacao inversa
x = inverseInterpolate([3,5,10], tol)
print ("\nRaiz da funcao f(x) por Interpolacao Inversa:\n" + str(x) + "\n")
