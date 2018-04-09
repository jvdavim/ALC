import numpy as np

def isSymmetric(a, tol=1e-8):
    return np.allclose(a, a.T, atol=tol)