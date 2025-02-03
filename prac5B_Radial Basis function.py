import numpy as np
from scipy.linalg import norm, pinv 
import matplotlib.pyplot as plt

class RBF:
    def  init (self, indim, numCenters, outdim): 
        self.indim = indim
        self.outdim = outdim 
        self.numCenters = numCenters
        self.centers = [np.random.uniform(-1, 1, indim) for i in range(numCenters)] 
        self.beta = 8
        self.W = np.random.random((self.numCenters, self.outdim))

    def _basisfunc(self, c, d): 
        assert len(d) == self.indim
        return np.exp(-self.beta * norm(c - d) ** 2)

    def _calcAct(self, X):
        # calculate activations of RBFs
        G = np.zeros((X.shape[0], self.numCenters), float) 
        for ci, c in enumerate(self.centers):
            for xi, x in enumerate(X):
                G[xi, ci] = self._basisfunc(c, x) 
        return G

    def train(self, X, Y):
        """ X: matrix of dimensions n x indim
        Y: column vector of dimension n x 1 """

        # choose random center vectors from training set
        rnd_idx = np.random.permutation(X.shape[0])[:self.numCenters] 
        self.centers = [X[i, :] for i in rnd_idx]

        print("centers", self.centers)
        # calculate activations of RBFs 
        G = self._calcAct(X)
        print(G)

        # calculate output weights (pseudoinverse) 
        self.W = np.dot(pinv(G), Y)

    def test(self, X):
        """ X: matrix of dimensions n x indim """

        G = self._calcAct(X) 
        Y = np.dot(G, self.W) 
        return Y


if   __name__  == '  main  ': 
    #	1D Example
    n = 100
 

    x = np.mgrid[-1:1:complex(0, n)].reshape(n, 1) 
    # set y and add random noise
    y = np.sin(3 * (x + 0.5) ** 3 - 1)
    # y += np.random.normal(0, 0.1, y.shape)

    # rbf regression
    rbf = RBF(1, 10, 1)
    rbf.train(x, y) 
    z = rbf.test(x)

    # plot original data 
    plt.figure(figsize=(12, 8)) 
    plt.plot(x, y, 'k-')

    # plot learned model 
    plt.plot(x, z, 'r-', linewidth=2)

    # plot rbfs
    plt.plot([c[0] for c in rbf.centers], np.zeros(rbf.numCenters), 'gs')

    for c in rbf.centers:
        # RF prediction lines
        cx = np.arange(c - 0.7, c + 0.7, 0.01)
        cy = [rbf._basisfunc(np.array([cx_]), np.array([c])) for cx_ in cx] 
        plt.plot(cx, cy, '-', color='gray', linewidth=0.2)

    plt.xlim(-1.2, 1.2) 
    plt.show()
