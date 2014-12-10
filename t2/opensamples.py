import numpy as np
import matplotlib.pyplot as plt
from scipy.io import readsav

def main():
	postx=readsav('samples_x1.sav', python_dict=True)
	postt=readsav('samples_t2.sav', python_dict=True)
	#alpha is the intercept and beta is the slope

	alpha=postx['postx1']['alpha']
	beta=postx['postx1']['beta']

	#similarly you can add for t2

main()



