import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.sparse.linalg as sla
import os
import time
from PIL import Image 

filepath = "./yalefaces/"
images=[]
for filename in os.listdir(filepath):
    img = np.array(plt.imread(filepath+filename))
    img = img.flatten()
    images.append(img)
I=np.array(images)

#for i in range(165):
#    plt.figure()
#    plt.imshow(images[i].reshape(243,320))
#    time.sleep(0.3)
#    plt.close()


mean_face = np.sum(I,axis=0)/I.shape[0]
mean_face.reshape(1,77760)
mean_face_img = mean_face.reshape(243,320)
#plt.imshow(mean_face_img)

I1=I-mean_face
I1.shape
u, s, vt = sla.svds(I1,k=100)
V=vt.transpose()



for p in range(5,100,5):
    V_p=np.zeros(V.shape,dtype=np.float)
    for i in range(p):
        V_p[:,i] = V[:,-(i+1)]
        
    Z = np.matmul(I1,V_p)
    X = mean_face + np.matmul(Z,V_p.transpose())
    
    path = "./Output/"
    for i in range(15):
        #plt.ion()
        #plt.figure()
        im=Image.fromarray(X[i].reshape(243,320))
        im.save(os.path.join(path+"Im_0"+str(i)+".gif"))
    input("p= "+str(p)+"; Press Enter to continue... ")