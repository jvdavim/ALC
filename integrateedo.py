from aux import np


def integrateedo(x0, method, N=3, h=0.1):
    if method == "euler":
        xk = x0
        tk = f(0, x0)
        c = 0
        while c < N:
            K1 = f(tk, xk)
            xk1 = xk + K1*h
            tk = (c+1)*h
            xk = xk1
            c += 1
        return xk
    elif method == "runge-kutta-2":
        xk = x0
        tk = f(0, x0)
        c = 0
        while c < N:
            K1 = f(tk, xk)
            K2 = f(tk + h, xk + h*K1)
            xk1 = xk + (h/2.0)*(K1+K2)
            tk = (c+1)*h
            xk = xk1
            c += 1
        return xk
    elif method == "runge-kutta-4":
        xk = x0
        tk = f(0, x0)
        c = 0
        while c < N:
            K1 = f(tk, xk)
            K2 = f(tk + h/2, xk + (h/2)*K1)
            K3 = f(tk + h/2, xk + (h/2)*K2)
            K4 = f(tk + h, xk + h*K3)
            xk1 = xk + (h/6)*(K1+2*K2+2*K3+K4)
            tk = (c+1)*h
            xk = xk1
            c += 1
        return xk
    return 0


# ------------------------------------- main ------------------------------------- #

# inputs
def f(t, x):
    return t + x
x0 = 0.0
N = 3
method = "runge-kutta-4"

# integrate edo
result = integrateedo(x0, method, N)
print(result)