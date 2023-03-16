import numpy as np
import math
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from sklearn.metrics import mean_squared_error
from skimage.metrics import structural_similarity as ssim
import cv2

path = "D:\\II FAC II\\Master 2\\Imagerie Computationnelle\\noise2noise\\res\\TESTS\\n2n-sat-30\\"

fichiers = [f for f in listdir(path) if isfile(join(path, f))]
ssim_x = 0

for i in range(4):
    x_origin = fichiers[i]
    x_pred = fichiers[i+4]

    print(x_origin + "    " + x_pred)
    x_origin = plt.imread(path + x_origin)
    x_pred = plt.imread(path + x_pred)

    #msenp = np.square(np.subtract(x_origin, x_pred)).mean()
    #mser = mean_squared_error(x_origin[:,:,0], x_pred[:,:,0])
    #mseg = mean_squared_error(x_origin[:,:,1], x_pred[:,:,1])
    #mseb = mean_squared_error(x_origin[:,:,2], x_pred[:,:,2])
    #mse = (mser + mseg + mseb) / 3
    
    if (len(x_origin.shape) > 2):
        x_origin = cv2.cvtColor(x_origin, cv2.COLOR_RGB2GRAY)
    if (len(x_pred.shape) > 2):    
        x_pred = cv2.cvtColor(x_pred, cv2.COLOR_RGB2GRAY)
    
    ssim_x += ssim(x_origin, x_pred)
    #psnr =  20 * math.log10(np.max(x_pred) / math.sqrt(mse))
    #psnr = 10 * math.log10(np.max(x_pred) / mse)
    #print("psnr = " + str(psnr))
    print("ssim = " + str(ssim_x))

print(ssim_x/4)