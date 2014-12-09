import numpy as np
import sys

from scipy.odr import *
from cosmoCalc import mod
from scipy.stats import pearsonr

def scatte(file, ind):
	ind_ls=[5, 7, 9]
	arr=np.loadtxt(file, usecols=(1, 3, ind_ls[ind], ind_ls[ind]+1), skiprows=1)
	t2=arr
	abs=t2[:,1]-np.array([mod(i) for i in t2[:,0]])
	abserr=np.loadtxt(file, usecols=(3, 4), skiprows=1)[:,1]

	rd=RealData(arr[:,2], abs, sx=arr[:,3], sy=abserr)
	def f(B, x):
		return	B[0]*x+B[1]
	f=Model(f)
	
	out=ODR(rd, f, beta0=[1., 2.])
	o1=out.run()
	print abserr, o1.beta, arr[:,2]
	corr=abs-(o1.beta[0]*arr[:,2]+o1.beta[1])
	return np.std(abs), np.std(corr), pearsonr(abs, arr[:,2])
def main():
	file='t2stan_csp.dat'
	print scatte(file, int(sys.argv[1]))
main()
