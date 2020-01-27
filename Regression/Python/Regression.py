'exec(%matplotlib inline)'

from __future__ import print_function
import numpy as np
from numpy import dot
from numpy.linalg import inv
from numpy.linalg import multi_dot as mdot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
# 3D plotting
###############################################################################
# Helper functions
def prepend_one(X):
#"""prepend a one vector to X."""
    return np.column_stack([np.ones(X.shape[0]), X])
def grid2d(start, end, num=50):
    dom = np.linspace(start, end, num)
    X0, X1 = np.meshgrid(dom, dom)
    return np.column_stack([X0.flatten(), X1.flatten()])

###############################################################################
# load the data
data = np.loadtxt("dataLinReg2D.txt")
print("data.shape:", data.shape)
# split into features and labels
X, y = data[:, :2], data[:, 2]
print("X.shape:", X.shape)
print("y.shape:", y.shape)
# 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # the projection arg is important!
ax.scatter(X[:, 0], X[:, 1], y, color="red")
ax.set_title("raw data")
plt.draw()
# show, use plt.show() for blocking
# prep for linear reg.
X = prepend_one(X)
print("X.shape:", X.shape)
# Fit model/compute optimal parameters beta
beta_ = mdot([inv(dot(X.T, X)), X.T, y])
print("Optimal beta:", beta_)
# prep for prediction
X_grid = prepend_one(grid2d(-3, 3, num=30))
print("X_grid.shape:", X_grid.shape)
# Predict with trained model
y_grid = dot(X_grid, beta_)
print("Y_grid.shape", y_grid.shape)
# visualize the result
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # the projection part is important
ax.scatter(X_grid[:, 1], X_grid[:, 2], y_grid) # dont use the 1 infront
ax.scatter(X[:, 1], X[:, 2], y, color="red") # also show the real data
ax.set_title("predicted data")
plt.show()
