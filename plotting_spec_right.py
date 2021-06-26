import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
#3D plot surface

plot3d=pd.read_csv("spectogram_rightCheek.csv", sep=";")


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(61)
Y = np.linspace(0.7, 2, 9)

X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
Z = plot3d.T

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel("times pwelch segments are averaged")
ax.set_ylabel("freq HZ")
ax.set_zlabel("magnitude power")
plt.title("Spectogram rightCheek")



# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)#
fig.set_size_inches(10, 10)


plt.show()
