from aux import np


def rkn(t0, x0, xd0, N=3, h=0.1):
    xk = x0
    xdk = xd0
    tk = f(t0, x0, xd0)
    c = 0
    while c < N:
        K1 = 1/2.0*h*f(tk, xk, xdk)
        Q = 1/2.0*h*(xdk+1/2.0*K1)
        K2 = 1/2.0*h*f(tk + h/2.0, xk + Q, xdk + K1)
        K3 = 1/2.0*h*f(tk + h/2.0, xk + Q, xdk + K2)
        L = h*(xdk + K3)
        K4 = 1/2.0*h*f(tk + h, xk + L, xdk + 2*K3)
        xk1 = xk + h*(xdk + 1/3.0*(K1 + K2 + K3))
        xdk1 = xdk + 1/3.0*(K1 + 2*K2 + 2*K3 + K4)
        tk = (c+1)*h
        xk = xk1
        xdk = xdk1
        c += 1
    return xk


# ------------------------------------- main ------------------------------------- #

# inputs
def f(t, x, xd):
    return - 9.8 - xd*abs(xd)
x0 = 0.0
xd0 = 0.0

# rkn
for N in range(11):
    n = rkn(0.0, x0, xd0, N)
    print(str(N) + ": " + str(n))