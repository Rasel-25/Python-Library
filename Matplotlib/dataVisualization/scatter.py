# rotational 3d plot
import numpy as np
import matplotlib.pyplot as plt

x=np.random.random(200)
y=np.random.random(200)
z=np.random.random(200)
plt.figure(figsize=(15,10))
axes=plt.axes(projection='3d') #Add an axes to the current figure and make it the current axes.
axes.scatter3D(x,y,z)  
axes.set_xlabel('x_axis')
axes.set_ylabel('y_axis')
axes.set_zlabel('z_axis')
plt.show()