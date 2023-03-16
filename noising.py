import numpy as np
import math
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join


def bruitage(i, snr) :
    #calcul de Pi
    pi = 0
    for k in range (0,i.shape[0]):
        for l in range(0, i.shape[1]):
            pi += (i[k][l]**2 )/(i.shape[0]*i.shape[1]) 

    #calcul de pib
    pib = pi / math.pow(10, snr/10)

    #création du bruit
    br = np.random.randn(i.shape[0],i.shape[1])

    #calcul de l'image bruitée
    ib = np.zeros(i.shape)
    for k in range (0,i.shape[0]):
        for l in range(0, i.shape[1]):
            new_val = i[k][l] + pib * br[k][l]
            if new_val > 255 : new_val = i[k][l] - pib * br[k][l]
            ib[k][l] = np.abs(new_val)

    return ib

def bsds300(snr=31.01) : 
    path = "D:\\II FAC II\\Master 2\\Imagerie Computationnelle\\noise2noise\\datasets\\BSDS300\\base"
    dest = "D:\\II FAC II\\Master 2\\Imagerie Computationnelle\\noise2noise\\datasets\\BSDS300\\noised"
    fichiers = [f for f in listdir(path) if isfile(join(path, f))]

    for fichier in fichiers :
        x = plt.imread(path + fichier)
        xb = np.copy(x)
        r = bruitage(x[:,:,0], snr)
        g = bruitage(x[:,:,1], snr)
        b = bruitage(x[:,:,2], snr)
        xb[:,:,0] = r
        xb[:,:,1] = g
        xb[:,:,2] = b

        plt.imsave(dest+"n"+fichier, xb)
        plt.clf()

def mri(snr=31.76) : 
    path = "D:\\II FAC II\\Master 2\\Imagerie Computationnelle\\noise2noise\\datasets\\MRI\\base"
    dest = "D:\\II FAC II\\Master 2\\Imagerie Computationnelle\\noise2noise\\datasets\MRI\\noised"
    fichiers = [f for f in listdir(path) if isfile(join(path, f))]

    for fichier in fichiers :
        x = plt.imread(path + fichier)
        if (len(x.shape) > 2):
            xb = np.copy(x[:,:,0])
        else : 
            xb = np.copy(x)
        xb = bruitage(xb, snr)
        xb = xb.astype(np.uint8)

        plt.imsave(dest+"n"+fichier, xb, cmap="gray")
        plt.clf()

def sat(snr=30) : 
    path = "D:\\II FAC II\\Master 2\\Imagerie Computationnelle\\noise2noise\\datasets\\SAT\\base"
    dest = "D:\\II FAC II\\Master 2\\Imagerie Computationnelle\\noise2noise\\datasets\\SAT\\noised"
    fichiers = [f for f in listdir(path) if isfile(join(path, f))]

    for fichier in fichiers :
        x = plt.imread(path + fichier)
        xb = np.copy(x)
        r = bruitage(x[:,:,0], snr)
        g = bruitage(x[:,:,1], snr)
        b = bruitage(x[:,:,2], snr)
        xb[:,:,0] = r
        xb[:,:,1] = g
        xb[:,:,2] = b

        plt.imsave(dest+"n"+fichier, xb)
        plt.clf()

#bsds300()
#mri()
#sat()

