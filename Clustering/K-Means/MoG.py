# %%
'exec(%matplotlib inline)'

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy.linalg as nla
import scipy as sp
import scipy.sparse.linalg as sla
import os
from PIL import Image


#%%
def gaussian(u,Sigma,x):
	G=(1/np.sqrt(nla.det(2*np.pi*Sigma)))*(np.power(np.e,(-0.5*np.matmul(np.matmul(np.transpose(x-u),nla.inv(Sigma)),(x-u)))))
	return G

#%%
data = pd.read_csv('mixture.txt',delimiter= '\\s+',header=None)
data = np.array(data.values)
N = data.shape[0]
d = data.shape[1]
K=3

clusters = []
q = np.zeros((N,K),dtype=float)
S = np.matmul(np.transpose(data),data)
Sigma = np.ones((K,d,d),dtype=float)
sum_classes = np.zeros(K,dtype=float)

#%%  Allocate random cluster intiliazizations

for i in range(K):
	  clusters.append(data[np.random.randint(0,N-1)])
	  Sigma[i] = S 

#%%	  
for iterations in range(10):  
	#Update probabilistic assignments
		  
	for i in range(N):
		q_sum = 0
		for k in range(K):
			q[i,k] = gaussian(clusters[k],Sigma[k],data[i])
			q_sum += q[i,k]
		q[i] = q[i]/q_sum
			
		
	# Update cluster parameters
	
	for k in range(K):
		sum_classes[k] = np.sum(q[:,k])
		u=0
		uk_ukT = np.matmul(np.transpose(clusters[k]),clusters[k])
		S=0
		for i in range(N):
			u += data[i]*q[i,k]
			S += q[i,k]*np.matmul(np.transpose(data[i]),data[i]) - uk_ukT
		clusters[k] = u/sum_classes[k]
		Sigma[k] = S/sum_classes[k]
