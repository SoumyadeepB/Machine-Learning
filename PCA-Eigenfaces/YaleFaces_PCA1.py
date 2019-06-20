import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.sparse.linalg as sla
import os
from PIL import Image 

filepath = "./yalefaces/"
images=[]
#Read the images
for filename in os.listdir(filepath):
    img = np.array(plt.imread(filepath+filename))
    img = img.flatten()  #Convert image to a vector
    images.append(img)
I=np.array(images)

path = "./Output/"
mean_face = np.sum(I,axis=0)/I.shape[0]  #Sum along the Columns / Total inputs
mean_face.reshape(1,77760)
plt.imshow(mean_face.reshape(243,320))

im=Image.fromarray(mean_face.reshape(243,320))
im.save(os.path.join(path+"Mean_face.gif"))
I1=I-mean_face
I1.shape
u, s, vt = sla.svds(I1,k=100) #which='LM' chooses the largest k 
V=vt.transpose()


error = []
for p in range(5,100,5):
    V_p=np.zeros(V.shape,dtype=np.float)
    for i in range(p):
        V_p[:,i] = V[:,-(i+1)]   # select the p highest eigen-vectors
        
    Z = np.matmul(I1,V_p)
    X = mean_face + np.matmul(Z,V_p.transpose())
    
    e=0
    for i in range(165):
        e +=  np.square(np.linalg.norm(I[i]-X[i]))
    
    error.append(e)
    
    for i in range(10):
        im=Image.fromarray(X[i].reshape(243,320))
        im.save(os.path.join(path+"Im_0"+str(i)+".gif"))
    input("p= "+str(p))
    
print(error)
plt.figure()
plt.xlabel('p')
plt.ylabel('Error')
plt.plot(range(5,100,5),error)

plt.savefig(path+'Error_Plot.jpg')
