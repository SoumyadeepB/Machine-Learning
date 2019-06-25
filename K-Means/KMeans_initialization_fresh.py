#%%
'exec(%matplotlib inline)'
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.sparse.linalg as sla
import os
from PIL import Image 

filepath = "./yalefaces_cropBackground/"
#Code to add .gif extension to files
# =============================================================================
# for filename in os.listdir(filepath):
#     src = filepath+''+filename 
#     dst = src + '.gif'
#     os.rename(src, dst)
# =============================================================================

images=[]
#Read the images
for filename in os.listdir(filepath):
    img = np.array(plt.imread(filepath+filename))
    imsize = img.shape
    img = img.flatten()  #Convert image to a vector
    images.append(img)
I=np.array(images)

R = imsize[0]
C = imsize[1]
N = I.shape[0]

cluster_label = np.zeros(N) # Cluster to which each image belongs

#%%
error_map = []
# Number of clusters : [2,10]
for K in range(2,11):

    for iteration in range(10):
        clusters = []
        # Allocate random clusters
        for i in range(K):
            clusters.append(I[np.random.randint(0,N-1)])
        clusters = np.array(clusters)
            
        # Associate cluster labels to each data point
        for i in range(N):
            error = 0
            min_error = 10**10
            for k in range(K):
                error = np.square(np.linalg.norm(I[i]-clusters[k]))
             #   print(str(k)+": "+str(error))
                if error<min_error:
                    min_error = error
                    cluster_label[i]=k
            #print("i = "+str(i)+": "+str(min_error)+" Label: "+str(cluster_label[i]))
        L=[]
        E=[]  
        
        #Update Cluster Center
        for k in range(K):
            # Find all data points with Clluster_Label = k
            index = np.array(np.where(cluster_label==k)).flatten() 
            L.append(index.size)
            sum_images=np.zeros((1,R*C*4))
            for i in index:
                sum_images += I[i]
            clusters[k] = np.divide(sum_images,len(index))
        
        # Calculating Errors for each iteration
        sum_errors=[]
        for k in range(K):
            
            sum1=0
            index = np.array(np.where(cluster_label==k)).flatten()
            for i in index:
                sum1 += np.divide(np.square(np.linalg.norm(I[i]-clusters[k])),10**6).round()
            if sum1==0:
                sum1=10**10
            sum_errors.append(sum1)
        
        print("-"*90)
        print("K: "+str(K))
        print("\nIteration: "+str(iteration+1)+" || " + str(L))
        print("Error: " + str(sum_errors))
        x=np.argmin(np.array(sum_errors))
        print("Best cluster: " +str(x+1))
        #error_map.append(sum_errors[x])
        for i in range(K):
            plt.subplot(1,K,i+1)
            plt.imshow(clusters[i].reshape(R,C,4))
            plt.xticks([])
            plt.yticks([])
            plt.show()
            plt.figure()
    error_map.append(sum_errors[x]*(10**6))

#%%
plt.plot(range(2,11),error_map)
plt.xlabel("K")
plt.ylabel("Error")
plt.savefig('./Outputs/Error_Plot.jpg')
    