import numpy as np
import astropy.io.fits as pyfits

## get 3d fits data of a specific line
specLine = '../tempS15AL/feb15/IRAM-DR21/3d_dr21_sio21_smooth'
hdu = pyfits.open(specLine+'.fits')
data = hdu[0].data
header = hdu[0].header
print len(data)
print header['CDELT3']

## create 3d array of zeros to store smoothed spectra
newData = np.zeros(shape=(len(data)/2,len(data[0]),len(data[0][0])),dtype=float)
print len(newData)

## smoothing of the velocity data
for a in range(0,len(data[0][0])):
    for b in range(0,len(data[0])):
        for c in range(0,len(newData)):
            av = 0.5*(data[2*c][b][a] + data[2*c+1][b][a])
            newData[c][b][a] = av

## store newData
newHeader = header
newHeader['CDELT3'] = 2.*header['CDELT3']
newHeader['CRPIX3'] = len(newData)/2
writeHdu = pyfits.PrimaryHDU(newData,newHeader)
writeHdu.writeto(specLine+'_smooth.fits',clobber='True')
