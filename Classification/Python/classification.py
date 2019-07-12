#%% Load Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data2class.txt',delimiter= '\\s+',header=None)
y=data[2]
plt.figure()
plt.scatter(data[0],data[1],c=y)


#%%
