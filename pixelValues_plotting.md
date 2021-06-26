```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```


```python
# pixel average values
df_pixelAvgValues_left=pd.read_csv('Pixel_Arr_leftCheek (20).csv',";")
df_pixelAvgValues_right=pd.read_csv('Pixel_Arr_rightCheek (17).csv',";")
df_pixelAvgValues_forehead=pd.read_csv('Pixel_Arr_forehead (8).csv',";")


```


```python
time = df_pixelAvgValues_left['time']
pixel_left = df_pixelAvgValues_left['Pixel leftCheek']
pixel_right = df_pixelAvgValues_right['Pixel rightCheek']
pixel_forehead = df_pixelAvgValues_forehead['Pixel forehead']

```


```python
plt.figure(figsize=(35,10)) 

plt.xlabel('time in seconds',  fontsize=30, labelpad = 30)
plt.ylabel('Average pixel value',  fontsize=30, labelpad = 30)
plt.plot(time,pixel_left, label='pixel leftCheek', c="blue")
plt.plot(time,pixel_right, label='pixel rightCheek', c="green")
plt.plot(time,pixel_forehead, label='pixel forehead', c ="red")
plt.xticks(fontsize= 20)
plt.yticks(fontsize= 20)
plt.legend(loc='lower right',  fontsize=20)
plt.title("Average pixel data per camera frame and area ", fontsize = 30, loc = "center", y= 1.05)
plt.grid(linewidth=0.8, alpha=0.2)

```


![png](output_3_0.png)



```python

```
