```python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
```


```python
plot1=pd.read_csv("spectogram_forehead (2).csv", sep=";")
plot1.shape
```




    (61, 9)




```python


fig, ax = plt.subplots()

# Make data.
X = np.arange(61)
Y = np.linspace(0.7, 2, 9)

X, Y = np.meshgrid(X, Y)
Z = plot1.T

# Plot the surface.
surf = ax.pcolormesh(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


ax.set_xlabel("times pwelch segments are averaged")
ax.set_ylabel("freq HZ")
plt.title("Spectrogram forehead")



# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.set_size_inches(10, 10)


plt.show()

```

    C:\Users\maroa\anaconda3\envs\ml\lib\site-packages\ipykernel_launcher.py:12: MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
      if sys.path[0] == '':
    


    
![png](output_2_1.png)
    



```python
plot2=pd.read_csv("spectogram_leftCheek (4).csv", sep=";")
plot2.shape
```




    (61, 9)




```python
fig, ax = plt.subplots()

# Make data.
X = np.arange(61)
Y = np.linspace(0.7, 2, 9)

X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
Z = plot2.T

# Plot the surface.
surf2 = ax.pcolormesh(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel("times pwelch segments are averaged")
ax.set_ylabel("freq HZ")
#ax.set_zlabel("magnitude power")
plt.title("Spectrogram leftCheek")



# Add a color bar which maps values to colors.
fig.colorbar(surf2, shrink=0.5, aspect=5)
fig.set_size_inches(10, 10)


plt.show()

```

    C:\Users\maroa\anaconda3\envs\ml\lib\site-packages\ipykernel_launcher.py:13: MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
      del sys.path[0]
    


    
![png](output_4_1.png)
    



```python
plot3=pd.read_csv("spectogram_rightCheek.csv", sep=";")
plot3.shape
```




    (61, 9)




```python
fig, ax = plt.subplots()

# Make data.
X = np.arange(61)
Y = np.linspace(0.7, 2, 9)

X, Y = np.meshgrid(X, Y)
Z = plot3.T

# Plot the surface.
surf3 = ax.pcolormesh(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


ax.set_xlabel("times pwelch segments are averaged")
ax.set_ylabel("freq HZ")
plt.title("Spectrogram rightCheek")



# Add a color bar which maps values to colors.
fig.colorbar(surf3, shrink=0.5, aspect=5)
fig.set_size_inches(10, 10)


plt.show()

```

    C:\Users\maroa\anaconda3\envs\ml\lib\site-packages\ipykernel_launcher.py:12: MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
      if sys.path[0] == '':
    


    
![png](output_6_1.png)
    



```python
allmag=pd.read_csv("spec_mag.csv", sep=";")
allmag.shape
```




    (199, 257)




```python
fig, ax = plt.subplots()

# Make data.
X = np.arange(199)
Y = np.arange(197)
X, Y = np.meshgrid(X, Y)

allmag=np.array(allmag)
Z = allmag[:,60:].T
#Z=allmag.T

# Plot the surface.
surf = ax.pcolormesh(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)#
fig.set_size_inches(10, 10)
ax.set_xlabel("times FFT is called")
ax.set_ylabel("freq bin")
plt.title("Spectrogram magnitude")


plt.show()


```

    C:\Users\maroa\anaconda3\envs\ml\lib\site-packages\ipykernel_launcher.py:14: MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
      
    


    
![png](output_8_1.png)
    



```python

```
