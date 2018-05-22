from aux import np, solveLinear
from lu import lu


def nladjust(B0, J0, x, y, tol=10e-7, NITER=100):
    '''Dado um vetor inicial x0 e uma tolerancia tol, retorna o vetor solucao do sistema de equacoes nao lineares'''
    tolk = 1
    vectorpb = B0
    matrixJ = J0
    vectorx = x
    vectory = y
    count = 0
    while (tolk > tol) and (count <= NITER):
        # Calcula vetor F(B)------------------------------------------------
        vectorF = np.array([[f(vectorpb[0, 0], vectorpb[1, 0], vectorx[0, 0], vectory[0, 0])]])
        for i in range(1,vectorx.shape[0]):
            vectorF = np.append(vectorF, np.array([[f(vectorpb[0, 0], vectorpb[1, 0], vectorx[i, 0], vectory[i, 0])]]), axis=0)
        # ------------------------------------------------------------------
        # Calcula vetor Delta B---------------------------------------------
        vectorDb = solveLinear(lu(np.dot(matrixJ.T, matrixJ)), np.dot(-1, np.dot(matrixJ.T, vectorF)))
        # ------------------------------------------------------------------
        # Atualiza o vetor B------------------------------------------------
        vectorb = vectorpb + vectorDb
        # ------------------------------------------------------------------
        # Atualiza o vetor pB para ser o passado da proxima iteracao--------
        vectorpb = vectorb
        # ------------------------------------------------------------------
        # Calcula a tolerancia da i-esima iteracao--------------------------
        tolk = np.linalg.norm(vectorDb) / np.linalg.norm(vectorb)
        # ------------------------------------------------------------------
        # Atualiza o Jacobiano com a regra de broyden
        vectornF = np.array([[f(vectorpb[0, 0], vectorpb[1, 0], vectorx[0, 0], vectory[0, 0])]])
        for i in range(1,vectorx.shape[0]):
            vectornF = np.append(vectornF, np.array([[f(vectorpb[0, 0], vectorpb[1, 0], vectorx[i, 0], vectory[i, 0])]]), axis=0)
        vectorY = vectornF - vectorF
        matrixJ = matrixJ + np.dot(vectorY - np.dot(matrixJ, vectorDb), vectorDb.T) / np.dot(vectorDb.T, vectorDb)
        # ------------------------------------------------------------------
        count += 1
    return vectorb


# ------------------------------------- main ------------------------------------- #

# inputs
x = np.array([[1], [2], [3]])
y = np.array([[1.995], [1.410], [1.260]])
B0 = np.array([[0], [1]])
J0 = np.array([[0,-3], [1.884,-3], [2.986,-3]])
def f(a, b, x, y):
    return np.exp((x**a)/b)-y

# metodo de newton
b = nladjust(B0, J0, x, y)
print ("\nResultado do ajuste nao linear:\n" + str(b) + "\n")