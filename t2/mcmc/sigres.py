import emcee
import numpy as np
import sys
import matplotlib.pyplot as plt

import triangle


def lnprior(theta):
	m, b = theta
        if -10.0 < m < 10.0 and -10.0 < b < 15.0:
		return 0.0
        return -np.inf

def lnlike(theta, x,xerr,  y, yerr):
	    m, b = theta
	    model = m * (x) + b
	    ex=m*(x+xerr)+b-m*(x)-b	
	    return -0.5*(np.sum( ((y-model)**2./((yerr)**2.+(ex)**2.))))


