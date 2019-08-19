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
K = 4 #Number of clusters
cluster_label = np.zeros(N) # Cluster to which each image belongs
clusters = []

#clusters.append(I[0])
#clusters.append(I[20])
#clusters.append(I[100])
#clusters.append(I[130])
for i in range(K):
    clusters.append(np.random.randint(0,255,(R*C*4)))

clusters = np.array(clusters)
for iterations in range(10):
    for i in range(N):
        error = 0
        min_error = 999999999
        for k in range(K):
            error = np.linalg.norm(I[i]-clusters[k])
         #   print(str(k)+": "+str(error))
            if error<min_error:
                min_error = error
                cluster_label[i]=k
        #print("i = "+str(i)+": "+str(min_error)+" Label: "+str(cluster_label[i]))
    L=[]    
    for k in range(K):
        index = np.array(np.where(cluster_label==k)).flatten()
        L.append(index.size)
        sum_images=np.zeros((1,R*C*4))
        for i in index:
            sum_images += I[i]
        clusters[k] = np.divide(sum_images,len(index))
    print(L)
    
    
for i in range(K):
    plt.imshow(clusters[i].reshape(R,C,4))
    plt.figure()
