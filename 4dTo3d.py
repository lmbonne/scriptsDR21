import numpy as np
import astropy.io.fits as pyfits

## file to transform
fitsName = 'dr21_n2hd.fits'
directory = '../tempS15AL/feb15/IRAM-DR21/'

## open hdufile and get data
hdu = pyfits.open(directory+fitsName)
hdu.info()
data = hdu[0].data[0]
header = hdu[0].header

## create new header and write to fits file
newHeader = header
del newHeader[25:30]
del newHeader[5]
writeHdu = pyfits.PrimaryHDU(data,newHeader)
writeHdu.write(directory + '3d_' + fitsName,clobber='True')
