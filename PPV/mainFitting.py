import numpy as np
import astropy.io.fits as pyfits
import velocityChannelsDR21feb15 as channels

## give the name of the spectral line to be fitted
specLine = '13co10'

## open the spectral 3d file and get data
spectralHdu = pyfits.open('../../tempS15AL/feb15/IRAM-DR21/3d_dr21_' + specLine + '.fits')
spectralData = spectralHdu[0].data

## get the details of the velocity channels
vBegin, vEnd, amount = channels.lineChannelDetails(specLine)
print vEnd
