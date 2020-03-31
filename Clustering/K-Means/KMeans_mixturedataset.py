'exec(%matplotlib inline)'
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.sparse.linalg as sla
import pandas as pd
from PIL import Image 


data = pd.read_csv('mixture.txt',delimiter= '\\s+',header=None)
data = np.array(data.values)
N = data.shape[0]
d = data.shape[1]

for K in range(2,10):
    cluster_label = np.zeros(N) # Cluster to which each image belongs
    clusters = []
    for i in range(K):
        clusters.append(data[np.random.randint(0,N)])
    clusters = np.array(clusters)
    cluster_error = 0
    cluster_error_prev =  0
    
    # Iterate 10 times for every K
    iterations=0
    while(1):        
        
        iterations += 1
        # Associate cluster labels to each data point
        for i in range(N):
            error = 0
            min_error = 10**10
            for k in range(K):
                error = np.square(np.linalg.norm(data[i]-clusters[k]))
                if error<min_error:
                    min_error = error
                    cluster_label[i]=k
        L=[]   
        error_sum = 0
        # Update CLuster centres
        
        for k in range(K):
            # Find all data points with Cluster_Label = k
            index = np.array(np.where(cluster_label==k)).flatten()
            L.append(index.size)
            
            sum_data=np.zeros((1,d))
            for i in index:
                sum_data += data[i]
                error_sum += np.square(np.linalg.norm(data[i]-clusters[k]))
            clusters[k] = np.divide(sum_data,len(index))
            
        cluster_error_prev = cluster_error
        cluster_error = error_sum
        if(abs(cluster_error_prev - cluster_error)<10**-6):
            break
        print("K: "+str(K)+" || Iteration: "+str(iterations+1)+" || " + str(L) + " ||  Error: "+str(cluster_error))
        
        plt.scatter(data[:,0],data[:,1],c=cluster_label,s=10, cmap='viridis')
        plt.scatter(clusters[:, 0], clusters[:, 1], c='red', s=100, alpha=0.8);
        plt.show()
        plt.figure()
        
#        for i in range(K):
#            plt.imshow(clusters[i].reshape(R,C,4))
#            plt.xticks([])
#            plt.yticks([])
#            plt.show()
#            plt.figure() 
