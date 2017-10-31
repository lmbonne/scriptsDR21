import numpy as np

#### DEFINITIONS TO FIT GAUSSIANS TO THE SPECTRA #####

## the 1d gaussian for fitting (x0: central velocity, sigma: width)
def gaussian1d(x,A,x0,sigma):
    return A*np.exp(-(x-x0)**2/(2.*sigma**2))

## a double 1d gaussian for fitting
def doubleGaussian1d(x,A1,x1,sigma1,A2,x2,sigma2):
    return A1*np.exp(-(x-x1)**2/(2.*sigma1**2)) + A2*np.exp(-(x-x2)**2/(2.*sigma2**2))
