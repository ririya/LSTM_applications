import math
import numpy as np

def doSomething(a):
    return a*2

def getXmap(Xlong, vmap, vocabSize, seqLen, offset):
    Xlong = Xlong[offset:]
    N = Xlong.shape[0];
    M = math.floor(N / seqLen)
    Xlong = Xlong[0:M * seqLen]
    Npad = Xlong.shape[0]
    Xmap = np.zeros(Npad)
    for i in range(1,vocabSize):
        indx = np.where(Xlong == vmap[i])
        Xmap[indx] = i
    Xmap = Xmap.reshape(M,seqLen)
    return Xmap

    #Xmap = reshape(Xmap, seqLen, []);

