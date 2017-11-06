import numpy as np

## function that returns the velocity channel information (vBegin, vEnd, amount) of a specific line
def lineChannelDetails(specLine):
    vBegin = 0.
    vEnd = 0.
    amount = 0.
    if(specLine == '13co10'):
        vBegin = 79.934         ## all velocities in km/s
        vEnd = -79.989
        amount = 1205. - 1.
    else:
        print 'An error has to be thrown' ## STILL THROW ERROR
    return vBegin, vEnd, amount
