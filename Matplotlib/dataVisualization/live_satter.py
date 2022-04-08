# rotational 3d plot
import numpy as np
import matplotlib.pyplot as plt

x=np.random.random(10)
y=np.random.random(10)
z=np.random.random(10)
X=[]
Y=[]
Z=[]
plt.figure(figsize=(15,10))
axes=plt.axes(projection='3d') 
for index in range(x.shape[0]):  #  x.shape[0]= 200 according to size of row
    X.append(x[index])
    Y.append(y[index])
    Z.append(z[index])
    axes.scatter3D(X,Y,Z)  

    axes.set_xlabel('x_axis')
    axes.set_ylabel('y_axis')
    axes.set_zlabel('z_axis')
    plt.pause(5) #Run the GUI event loop for *interval* seconds.
plt.show()