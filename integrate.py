from aux import np, solveLinear
from lu import lu


def integrate(a, b, NP, method):
    if method == "polinomial":
        #Encontra vetor x-------------------------------------
        vectorx = np.zeros(NP)
        if NP == 1:
            vectorx[0] = (a+b)/2
        else:
            Dx = (b-a)/(NP-1)
            for i in range(NP):
                vectorx[i] = a + (i)*Dx
        #------------------------------------------------------
        #Inicializa matriz x e vetor ab e vetor F--------------
        matrixx = np.zeros((NP, NP))
        vectorba = np.zeros((NP, 1))
        vectorF = np.zeros((NP, 1))
        for i in range(NP):
            matrixx[i] = np.power(vectorx, i)
            vectorba[i] = ((b**(i+1)) - (a**(i+1))) / (i+1)
            vectorF[i] = f(vectorx[i])
        #------------------------------------------------------
        #Computa o vetor de pesos w----------------------------
        vectorw = solveLinear(lu(matrixx), vectorba)
        #------------------------------------------------------
        return np.dot(vectorF.T, vectorw)[0,0]


    elif method == "quadratura":
        if NP > 10:
            print("So pode menor ou igual a 10 pq tem na tabela.")
            return 0
        #Tabela o vetor de pesos w----------------------------
        if NP == 2:
            vectorw = np.array([1, 1])
            vectorx = np.array([-0.577, 0.577])
        elif NP == 3:
            vectorw = np.array([0.889, 0.556, 0.556])
            vectorx = np.array([0, -0,775, 0.775])
        elif NP == 4:
            vectorw = np.array([0.652, 0.652, 0.348, 0.348])
            vectorx = np.array([-0.340, 0.340, -0.861, 0.861])
        elif NP == 5:
            vectorw = np.array([0.569, 0.477, 0.477, 0.237, 0.237])
            vectorx = np.array([0, -0.538, 0.538, -0.906, 0.906])
        elif NP == 6:
            vectorw = np.array([0.361, 0.361, 0.468, 0.468, 0.171, 0.171])
            vectorx = np.array([0.661, -0.661, -0.239, 0.239, -0.932, 0.932])
        elif NP == 7:
            vectorw = np.array([0.462, 0.382, 0.382, 0.280, 0.280, 0.129, 0.129])
            vectorx = np.array([0, 0.406, -0.406, -0.742, 0.742, -0.949, 0.949])
        elif NP == 8:
            vectorw = np.array([0.363, 0.363, 0.314, 0.314, 0.222, 0.222, 0.101, 0.101])
            vectorx = np.array([-0.183, 0.183, -0.526, 0.526, -0.797, 0.797, -0.960, 0.960])
        elif NP == 9:
            vectorw = np.array([0.330, 0.181, 0.181, 0.081, 0.081, 0.312, 0.312, 0.261, 0.261])
            vectorx = np.array([0, -0.836, 0.836, -0.968, 0.968, -0.324, 0.324, -0.613, 0.613])
        elif NP == 10:
            vectorw = np.array([0.296, 0.296, 0.269, 0.269, 0.219, 0.219, 0.149, 0.149, 0.067, 0.067])
            vectorx = np.array([-0.149, 0.149, -0.433, 0.433, -0.679, 0.679, -0.865, 0.865, -0.974, 0.974])
        #------------------------------------------------------
        vectorF = np.zeros((NP, 1))
        for i in range(NP):
            vectorF[i] = f((a+b+(b-a)*vectorx[i])/2)
        return (np.dot(vectorF.T, vectorw)*(b-a))[0]/2
    return 0

# ------------------------------------- main ------------------------------------- #

# inputs
def f(x):
    return (2+x+2*(x**2))


# integrate polinomial
A = integrate(1, 3, 2, "quadratura")
print(A)