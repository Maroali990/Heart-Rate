```python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
```


```python
plot1=pd.read_csv("Magnitude_avgforehead (7).csv", sep=";")
plot1.shape
plot12=plot1.iloc[:,1:313]
freq=plot1.iloc[:,0]
plot12
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>magnitude2</th>
      <th>magnitude3</th>
      <th>magnitude4</th>
      <th>magnitude5</th>
      <th>magnitude6</th>
      <th>magnitude7</th>
      <th>magnitude8</th>
      <th>magnitude9</th>
      <th>magnitude10</th>
      <th>magnitude11</th>
      <th>...</th>
      <th>magnitude304</th>
      <th>magnitude305</th>
      <th>magnitude306</th>
      <th>magnitude307</th>
      <th>magnitude308</th>
      <th>magnitude309</th>
      <th>magnitude310</th>
      <th>magnitude311</th>
      <th>magnitude312</th>
      <th>magnitude313</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17.734710</td>
      <td>16.938273</td>
      <td>16.176704</td>
      <td>15.467032</td>
      <td>14.769214</td>
      <td>14.098912</td>
      <td>13.516517</td>
      <td>13.080895</td>
      <td>12.905456</td>
      <td>12.771106</td>
      <td>...</td>
      <td>22.212677</td>
      <td>22.221867</td>
      <td>22.222750</td>
      <td>22.326466</td>
      <td>22.189233</td>
      <td>22.070453</td>
      <td>21.864829</td>
      <td>21.567479</td>
      <td>21.232021</td>
      <td>20.817436</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13.439866</td>
      <td>12.800619</td>
      <td>12.183746</td>
      <td>11.595211</td>
      <td>11.075402</td>
      <td>10.556557</td>
      <td>10.075057</td>
      <td>9.699967</td>
      <td>9.704466</td>
      <td>9.710865</td>
      <td>...</td>
      <td>16.146351</td>
      <td>16.092829</td>
      <td>16.204904</td>
      <td>16.122042</td>
      <td>16.323661</td>
      <td>16.430625</td>
      <td>16.535969</td>
      <td>16.638954</td>
      <td>16.711980</td>
      <td>16.818738</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20.314618</td>
      <td>20.086775</td>
      <td>19.788385</td>
      <td>19.444066</td>
      <td>19.041508</td>
      <td>18.678050</td>
      <td>18.275701</td>
      <td>17.785638</td>
      <td>17.618062</td>
      <td>17.480534</td>
      <td>...</td>
      <td>19.380352</td>
      <td>19.901482</td>
      <td>20.246460</td>
      <td>20.864496</td>
      <td>21.421334</td>
      <td>22.020146</td>
      <td>22.655660</td>
      <td>23.287962</td>
      <td>23.947880</td>
      <td>24.556855</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24.180794</td>
      <td>23.953674</td>
      <td>23.662001</td>
      <td>23.307713</td>
      <td>22.945753</td>
      <td>22.522120</td>
      <td>22.174053</td>
      <td>21.757733</td>
      <td>21.557026</td>
      <td>21.505498</td>
      <td>...</td>
      <td>8.521742</td>
      <td>8.827417</td>
      <td>9.294671</td>
      <td>9.889424</td>
      <td>10.539684</td>
      <td>11.401692</td>
      <td>12.304928</td>
      <td>13.288306</td>
      <td>14.290529</td>
      <td>15.362272</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25.022752</td>
      <td>24.897053</td>
      <td>24.728391</td>
      <td>24.523723</td>
      <td>24.317567</td>
      <td>24.102665</td>
      <td>23.889944</td>
      <td>23.675805</td>
      <td>23.701516</td>
      <td>23.922907</td>
      <td>...</td>
      <td>11.329550</td>
      <td>11.824597</td>
      <td>12.480727</td>
      <td>13.033180</td>
      <td>13.853027</td>
      <td>14.528477</td>
      <td>15.234792</td>
      <td>15.893045</td>
      <td>16.552771</td>
      <td>17.142271</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.154080</td>
      <td>25.426159</td>
      <td>25.626713</td>
      <td>25.769769</td>
      <td>25.788407</td>
      <td>25.751003</td>
      <td>25.613749</td>
      <td>25.508207</td>
      <td>25.450142</td>
      <td>25.814190</td>
      <td>...</td>
      <td>11.153371</td>
      <td>11.453572</td>
      <td>11.789728</td>
      <td>12.167502</td>
      <td>12.490434</td>
      <td>12.818341</td>
      <td>13.086232</td>
      <td>13.296975</td>
      <td>13.406458</td>
      <td>13.438714</td>
    </tr>
    <tr>
      <th>6</th>
      <td>24.814653</td>
      <td>25.011629</td>
      <td>25.143352</td>
      <td>25.237506</td>
      <td>25.266806</td>
      <td>25.292636</td>
      <td>25.292227</td>
      <td>25.299536</td>
      <td>25.385966</td>
      <td>25.731219</td>
      <td>...</td>
      <td>9.115640</td>
      <td>9.401029</td>
      <td>9.681379</td>
      <td>10.011253</td>
      <td>10.355687</td>
      <td>10.716269</td>
      <td>11.064564</td>
      <td>11.409954</td>
      <td>11.759529</td>
      <td>12.103065</td>
    </tr>
    <tr>
      <th>7</th>
      <td>24.057803</td>
      <td>23.925519</td>
      <td>23.735538</td>
      <td>23.499764</td>
      <td>23.218182</td>
      <td>22.964665</td>
      <td>22.677285</td>
      <td>22.482881</td>
      <td>22.346504</td>
      <td>22.479311</td>
      <td>...</td>
      <td>11.652895</td>
      <td>11.666748</td>
      <td>11.777005</td>
      <td>11.871154</td>
      <td>12.064840</td>
      <td>12.250238</td>
      <td>12.460422</td>
      <td>12.682163</td>
      <td>12.895570</td>
      <td>13.117411</td>
    </tr>
    <tr>
      <th>8</th>
      <td>23.065086</td>
      <td>22.941661</td>
      <td>22.760746</td>
      <td>22.528932</td>
      <td>22.304174</td>
      <td>22.037191</td>
      <td>21.808056</td>
      <td>21.568887</td>
      <td>21.430133</td>
      <td>21.331191</td>
      <td>...</td>
      <td>10.165808</td>
      <td>10.111475</td>
      <td>10.062105</td>
      <td>10.069252</td>
      <td>10.031456</td>
      <td>10.050197</td>
      <td>10.051120</td>
      <td>10.049252</td>
      <td>10.055124</td>
      <td>10.047433</td>
    </tr>
    <tr>
      <th>9</th>
      <td>17.893490</td>
      <td>17.920959</td>
      <td>17.895463</td>
      <td>17.834342</td>
      <td>17.739115</td>
      <td>17.643133</td>
      <td>17.570219</td>
      <td>17.560957</td>
      <td>17.498134</td>
      <td>17.683131</td>
      <td>...</td>
      <td>8.132669</td>
      <td>8.046184</td>
      <td>7.903493</td>
      <td>7.737574</td>
      <td>7.595514</td>
      <td>7.382083</td>
      <td>7.155110</td>
      <td>6.908510</td>
      <td>6.642023</td>
      <td>6.391652</td>
    </tr>
    <tr>
      <th>10</th>
      <td>13.515544</td>
      <td>13.590065</td>
      <td>13.615214</td>
      <td>13.599436</td>
      <td>13.544418</td>
      <td>13.511542</td>
      <td>13.449702</td>
      <td>13.481124</td>
      <td>13.569670</td>
      <td>13.793675</td>
      <td>...</td>
      <td>8.427458</td>
      <td>8.320808</td>
      <td>8.178002</td>
      <td>8.037379</td>
      <td>7.927618</td>
      <td>7.781519</td>
      <td>7.614571</td>
      <td>7.445183</td>
      <td>7.269889</td>
      <td>7.076487</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11.509263</td>
      <td>11.510000</td>
      <td>11.483503</td>
      <td>11.439694</td>
      <td>11.398204</td>
      <td>11.363685</td>
      <td>11.306451</td>
      <td>11.375990</td>
      <td>11.379698</td>
      <td>11.652277</td>
      <td>...</td>
      <td>5.539794</td>
      <td>5.516426</td>
      <td>5.511794</td>
      <td>5.493884</td>
      <td>5.475836</td>
      <td>5.475085</td>
      <td>5.483171</td>
      <td>5.490120</td>
      <td>5.501948</td>
      <td>5.534723</td>
    </tr>
    <tr>
      <th>12</th>
      <td>9.410606</td>
      <td>9.237763</td>
      <td>9.046741</td>
      <td>8.853329</td>
      <td>8.678350</td>
      <td>8.476771</td>
      <td>8.284809</td>
      <td>8.194709</td>
      <td>8.155714</td>
      <td>8.072772</td>
      <td>...</td>
      <td>6.165073</td>
      <td>6.110612</td>
      <td>6.062630</td>
      <td>6.057394</td>
      <td>6.066167</td>
      <td>6.053944</td>
      <td>6.027942</td>
      <td>5.995412</td>
      <td>5.954719</td>
      <td>5.893913</td>
    </tr>
    <tr>
      <th>13</th>
      <td>10.374504</td>
      <td>10.163767</td>
      <td>9.908579</td>
      <td>9.625096</td>
      <td>9.310104</td>
      <td>9.024277</td>
      <td>8.778231</td>
      <td>8.526813</td>
      <td>8.339971</td>
      <td>8.410311</td>
      <td>...</td>
      <td>4.334447</td>
      <td>4.385934</td>
      <td>4.436786</td>
      <td>4.471384</td>
      <td>4.526685</td>
      <td>4.589494</td>
      <td>4.652529</td>
      <td>4.706480</td>
      <td>4.751087</td>
      <td>4.795239</td>
    </tr>
    <tr>
      <th>14</th>
      <td>10.598395</td>
      <td>10.227719</td>
      <td>9.855743</td>
      <td>9.494803</td>
      <td>9.172785</td>
      <td>8.870647</td>
      <td>8.586216</td>
      <td>8.370011</td>
      <td>8.248949</td>
      <td>8.426622</td>
      <td>...</td>
      <td>3.930916</td>
      <td>4.068992</td>
      <td>4.248105</td>
      <td>4.462537</td>
      <td>4.675403</td>
      <td>4.885600</td>
      <td>5.084050</td>
      <td>5.272859</td>
      <td>5.447794</td>
      <td>5.599003</td>
    </tr>
    <tr>
      <th>15</th>
      <td>10.455588</td>
      <td>9.871314</td>
      <td>9.311928</td>
      <td>8.788985</td>
      <td>8.308580</td>
      <td>7.877712</td>
      <td>7.523343</td>
      <td>7.340025</td>
      <td>7.186029</td>
      <td>7.239927</td>
      <td>...</td>
      <td>4.577066</td>
      <td>4.769466</td>
      <td>5.005986</td>
      <td>5.314896</td>
      <td>5.694099</td>
      <td>6.014498</td>
      <td>6.321764</td>
      <td>6.607251</td>
      <td>6.870764</td>
      <td>7.113991</td>
    </tr>
    <tr>
      <th>16</th>
      <td>11.156948</td>
      <td>10.568214</td>
      <td>9.995799</td>
      <td>9.451512</td>
      <td>8.927263</td>
      <td>8.461432</td>
      <td>8.065962</td>
      <td>7.765238</td>
      <td>7.573031</td>
      <td>7.512801</td>
      <td>...</td>
      <td>2.786694</td>
      <td>2.940304</td>
      <td>3.090982</td>
      <td>3.253397</td>
      <td>3.452880</td>
      <td>3.731228</td>
      <td>4.012881</td>
      <td>4.290539</td>
      <td>4.557088</td>
      <td>4.804846</td>
    </tr>
    <tr>
      <th>17</th>
      <td>9.811692</td>
      <td>9.402548</td>
      <td>8.993455</td>
      <td>8.597338</td>
      <td>8.240904</td>
      <td>7.915641</td>
      <td>7.625070</td>
      <td>7.364729</td>
      <td>7.176947</td>
      <td>7.165343</td>
      <td>...</td>
      <td>4.887898</td>
      <td>5.058781</td>
      <td>5.253823</td>
      <td>5.454284</td>
      <td>5.653675</td>
      <td>5.842247</td>
      <td>6.033506</td>
      <td>6.224445</td>
      <td>6.411483</td>
      <td>6.593974</td>
    </tr>
    <tr>
      <th>18</th>
      <td>7.456991</td>
      <td>7.299968</td>
      <td>7.113823</td>
      <td>6.908161</td>
      <td>6.689925</td>
      <td>6.470912</td>
      <td>6.264475</td>
      <td>6.166732</td>
      <td>6.108094</td>
      <td>6.254601</td>
      <td>...</td>
      <td>4.956514</td>
      <td>5.002743</td>
      <td>5.083952</td>
      <td>5.208605</td>
      <td>5.375140</td>
      <td>5.537127</td>
      <td>5.694327</td>
      <td>5.842809</td>
      <td>5.981164</td>
      <td>6.103932</td>
    </tr>
    <tr>
      <th>19</th>
      <td>6.842899</td>
      <td>6.703936</td>
      <td>6.547900</td>
      <td>6.382626</td>
      <td>6.212350</td>
      <td>6.051760</td>
      <td>5.910220</td>
      <td>5.793772</td>
      <td>5.722824</td>
      <td>5.770515</td>
      <td>...</td>
      <td>5.305710</td>
      <td>5.342902</td>
      <td>5.380088</td>
      <td>5.419069</td>
      <td>5.461800</td>
      <td>5.535933</td>
      <td>5.603478</td>
      <td>5.663849</td>
      <td>5.715477</td>
      <td>5.761320</td>
    </tr>
  </tbody>
</table>
<p>20 rows × 312 columns</p>
</div>




```python


fig, ax = plt.subplots()

# Make data.
X = freq
#Y = np.linspace(0.7, 2, 9)
Y=np.arange(312)

X, Y = np.meshgrid(X, Y)
Z = plot12.T

# Plot the surface.
surf = ax.pcolormesh(Y, X, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


ax.set_xlabel("times pwelch segments are averaged")
ax.set_ylabel("frequency")
plt.title("Spectrogram forehead")



# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.set_size_inches(10, 10)


plt.show()

```

    C:\Users\maroa\anaconda3\envs\ml\lib\site-packages\ipykernel_launcher.py:13: MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
      del sys.path[0]
    


    
![png](output_2_1.png)
    



```python
plot2=pd.read_csv("Magnitude_avgleftCheek (13).csv", sep=";")
plot2.shape
plot22=plot1.iloc[:,1:313]
freq2=plot2.iloc[:,0]
plot22
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>magnitude2</th>
      <th>magnitude3</th>
      <th>magnitude4</th>
      <th>magnitude5</th>
      <th>magnitude6</th>
      <th>magnitude7</th>
      <th>magnitude8</th>
      <th>magnitude9</th>
      <th>magnitude10</th>
      <th>magnitude11</th>
      <th>...</th>
      <th>magnitude304</th>
      <th>magnitude305</th>
      <th>magnitude306</th>
      <th>magnitude307</th>
      <th>magnitude308</th>
      <th>magnitude309</th>
      <th>magnitude310</th>
      <th>magnitude311</th>
      <th>magnitude312</th>
      <th>magnitude313</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17.734710</td>
      <td>16.938273</td>
      <td>16.176704</td>
      <td>15.467032</td>
      <td>14.769214</td>
      <td>14.098912</td>
      <td>13.516517</td>
      <td>13.080895</td>
      <td>12.905456</td>
      <td>12.771106</td>
      <td>...</td>
      <td>22.212677</td>
      <td>22.221867</td>
      <td>22.222750</td>
      <td>22.326466</td>
      <td>22.189233</td>
      <td>22.070453</td>
      <td>21.864829</td>
      <td>21.567479</td>
      <td>21.232021</td>
      <td>20.817436</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13.439866</td>
      <td>12.800619</td>
      <td>12.183746</td>
      <td>11.595211</td>
      <td>11.075402</td>
      <td>10.556557</td>
      <td>10.075057</td>
      <td>9.699967</td>
      <td>9.704466</td>
      <td>9.710865</td>
      <td>...</td>
      <td>16.146351</td>
      <td>16.092829</td>
      <td>16.204904</td>
      <td>16.122042</td>
      <td>16.323661</td>
      <td>16.430625</td>
      <td>16.535969</td>
      <td>16.638954</td>
      <td>16.711980</td>
      <td>16.818738</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20.314618</td>
      <td>20.086775</td>
      <td>19.788385</td>
      <td>19.444066</td>
      <td>19.041508</td>
      <td>18.678050</td>
      <td>18.275701</td>
      <td>17.785638</td>
      <td>17.618062</td>
      <td>17.480534</td>
      <td>...</td>
      <td>19.380352</td>
      <td>19.901482</td>
      <td>20.246460</td>
      <td>20.864496</td>
      <td>21.421334</td>
      <td>22.020146</td>
      <td>22.655660</td>
      <td>23.287962</td>
      <td>23.947880</td>
      <td>24.556855</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24.180794</td>
      <td>23.953674</td>
      <td>23.662001</td>
      <td>23.307713</td>
      <td>22.945753</td>
      <td>22.522120</td>
      <td>22.174053</td>
      <td>21.757733</td>
      <td>21.557026</td>
      <td>21.505498</td>
      <td>...</td>
      <td>8.521742</td>
      <td>8.827417</td>
      <td>9.294671</td>
      <td>9.889424</td>
      <td>10.539684</td>
      <td>11.401692</td>
      <td>12.304928</td>
      <td>13.288306</td>
      <td>14.290529</td>
      <td>15.362272</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25.022752</td>
      <td>24.897053</td>
      <td>24.728391</td>
      <td>24.523723</td>
      <td>24.317567</td>
      <td>24.102665</td>
      <td>23.889944</td>
      <td>23.675805</td>
      <td>23.701516</td>
      <td>23.922907</td>
      <td>...</td>
      <td>11.329550</td>
      <td>11.824597</td>
      <td>12.480727</td>
      <td>13.033180</td>
      <td>13.853027</td>
      <td>14.528477</td>
      <td>15.234792</td>
      <td>15.893045</td>
      <td>16.552771</td>
      <td>17.142271</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.154080</td>
      <td>25.426159</td>
      <td>25.626713</td>
      <td>25.769769</td>
      <td>25.788407</td>
      <td>25.751003</td>
      <td>25.613749</td>
      <td>25.508207</td>
      <td>25.450142</td>
      <td>25.814190</td>
      <td>...</td>
      <td>11.153371</td>
      <td>11.453572</td>
      <td>11.789728</td>
      <td>12.167502</td>
      <td>12.490434</td>
      <td>12.818341</td>
      <td>13.086232</td>
      <td>13.296975</td>
      <td>13.406458</td>
      <td>13.438714</td>
    </tr>
    <tr>
      <th>6</th>
      <td>24.814653</td>
      <td>25.011629</td>
      <td>25.143352</td>
      <td>25.237506</td>
      <td>25.266806</td>
      <td>25.292636</td>
      <td>25.292227</td>
      <td>25.299536</td>
      <td>25.385966</td>
      <td>25.731219</td>
      <td>...</td>
      <td>9.115640</td>
      <td>9.401029</td>
      <td>9.681379</td>
      <td>10.011253</td>
      <td>10.355687</td>
      <td>10.716269</td>
      <td>11.064564</td>
      <td>11.409954</td>
      <td>11.759529</td>
      <td>12.103065</td>
    </tr>
    <tr>
      <th>7</th>
      <td>24.057803</td>
      <td>23.925519</td>
      <td>23.735538</td>
      <td>23.499764</td>
      <td>23.218182</td>
      <td>22.964665</td>
      <td>22.677285</td>
      <td>22.482881</td>
      <td>22.346504</td>
      <td>22.479311</td>
      <td>...</td>
      <td>11.652895</td>
      <td>11.666748</td>
      <td>11.777005</td>
      <td>11.871154</td>
      <td>12.064840</td>
      <td>12.250238</td>
      <td>12.460422</td>
      <td>12.682163</td>
      <td>12.895570</td>
      <td>13.117411</td>
    </tr>
    <tr>
      <th>8</th>
      <td>23.065086</td>
      <td>22.941661</td>
      <td>22.760746</td>
      <td>22.528932</td>
      <td>22.304174</td>
      <td>22.037191</td>
      <td>21.808056</td>
      <td>21.568887</td>
      <td>21.430133</td>
      <td>21.331191</td>
      <td>...</td>
      <td>10.165808</td>
      <td>10.111475</td>
      <td>10.062105</td>
      <td>10.069252</td>
      <td>10.031456</td>
      <td>10.050197</td>
      <td>10.051120</td>
      <td>10.049252</td>
      <td>10.055124</td>
      <td>10.047433</td>
    </tr>
    <tr>
      <th>9</th>
      <td>17.893490</td>
      <td>17.920959</td>
      <td>17.895463</td>
      <td>17.834342</td>
      <td>17.739115</td>
      <td>17.643133</td>
      <td>17.570219</td>
      <td>17.560957</td>
      <td>17.498134</td>
      <td>17.683131</td>
      <td>...</td>
      <td>8.132669</td>
      <td>8.046184</td>
      <td>7.903493</td>
      <td>7.737574</td>
      <td>7.595514</td>
      <td>7.382083</td>
      <td>7.155110</td>
      <td>6.908510</td>
      <td>6.642023</td>
      <td>6.391652</td>
    </tr>
    <tr>
      <th>10</th>
      <td>13.515544</td>
      <td>13.590065</td>
      <td>13.615214</td>
      <td>13.599436</td>
      <td>13.544418</td>
      <td>13.511542</td>
      <td>13.449702</td>
      <td>13.481124</td>
      <td>13.569670</td>
      <td>13.793675</td>
      <td>...</td>
      <td>8.427458</td>
      <td>8.320808</td>
      <td>8.178002</td>
      <td>8.037379</td>
      <td>7.927618</td>
      <td>7.781519</td>
      <td>7.614571</td>
      <td>7.445183</td>
      <td>7.269889</td>
      <td>7.076487</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11.509263</td>
      <td>11.510000</td>
      <td>11.483503</td>
      <td>11.439694</td>
      <td>11.398204</td>
      <td>11.363685</td>
      <td>11.306451</td>
      <td>11.375990</td>
      <td>11.379698</td>
      <td>11.652277</td>
      <td>...</td>
      <td>5.539794</td>
      <td>5.516426</td>
      <td>5.511794</td>
      <td>5.493884</td>
      <td>5.475836</td>
      <td>5.475085</td>
      <td>5.483171</td>
      <td>5.490120</td>
      <td>5.501948</td>
      <td>5.534723</td>
    </tr>
    <tr>
      <th>12</th>
      <td>9.410606</td>
      <td>9.237763</td>
      <td>9.046741</td>
      <td>8.853329</td>
      <td>8.678350</td>
      <td>8.476771</td>
      <td>8.284809</td>
      <td>8.194709</td>
      <td>8.155714</td>
      <td>8.072772</td>
      <td>...</td>
      <td>6.165073</td>
      <td>6.110612</td>
      <td>6.062630</td>
      <td>6.057394</td>
      <td>6.066167</td>
      <td>6.053944</td>
      <td>6.027942</td>
      <td>5.995412</td>
      <td>5.954719</td>
      <td>5.893913</td>
    </tr>
    <tr>
      <th>13</th>
      <td>10.374504</td>
      <td>10.163767</td>
      <td>9.908579</td>
      <td>9.625096</td>
      <td>9.310104</td>
      <td>9.024277</td>
      <td>8.778231</td>
      <td>8.526813</td>
      <td>8.339971</td>
      <td>8.410311</td>
      <td>...</td>
      <td>4.334447</td>
      <td>4.385934</td>
      <td>4.436786</td>
      <td>4.471384</td>
      <td>4.526685</td>
      <td>4.589494</td>
      <td>4.652529</td>
      <td>4.706480</td>
      <td>4.751087</td>
      <td>4.795239</td>
    </tr>
    <tr>
      <th>14</th>
      <td>10.598395</td>
      <td>10.227719</td>
      <td>9.855743</td>
      <td>9.494803</td>
      <td>9.172785</td>
      <td>8.870647</td>
      <td>8.586216</td>
      <td>8.370011</td>
      <td>8.248949</td>
      <td>8.426622</td>
      <td>...</td>
      <td>3.930916</td>
      <td>4.068992</td>
      <td>4.248105</td>
      <td>4.462537</td>
      <td>4.675403</td>
      <td>4.885600</td>
      <td>5.084050</td>
      <td>5.272859</td>
      <td>5.447794</td>
      <td>5.599003</td>
    </tr>
    <tr>
      <th>15</th>
      <td>10.455588</td>
      <td>9.871314</td>
      <td>9.311928</td>
      <td>8.788985</td>
      <td>8.308580</td>
      <td>7.877712</td>
      <td>7.523343</td>
      <td>7.340025</td>
      <td>7.186029</td>
      <td>7.239927</td>
      <td>...</td>
      <td>4.577066</td>
      <td>4.769466</td>
      <td>5.005986</td>
      <td>5.314896</td>
      <td>5.694099</td>
      <td>6.014498</td>
      <td>6.321764</td>
      <td>6.607251</td>
      <td>6.870764</td>
      <td>7.113991</td>
    </tr>
    <tr>
      <th>16</th>
      <td>11.156948</td>
      <td>10.568214</td>
      <td>9.995799</td>
      <td>9.451512</td>
      <td>8.927263</td>
      <td>8.461432</td>
      <td>8.065962</td>
      <td>7.765238</td>
      <td>7.573031</td>
      <td>7.512801</td>
      <td>...</td>
      <td>2.786694</td>
      <td>2.940304</td>
      <td>3.090982</td>
      <td>3.253397</td>
      <td>3.452880</td>
      <td>3.731228</td>
      <td>4.012881</td>
      <td>4.290539</td>
      <td>4.557088</td>
      <td>4.804846</td>
    </tr>
    <tr>
      <th>17</th>
      <td>9.811692</td>
      <td>9.402548</td>
      <td>8.993455</td>
      <td>8.597338</td>
      <td>8.240904</td>
      <td>7.915641</td>
      <td>7.625070</td>
      <td>7.364729</td>
      <td>7.176947</td>
      <td>7.165343</td>
      <td>...</td>
      <td>4.887898</td>
      <td>5.058781</td>
      <td>5.253823</td>
      <td>5.454284</td>
      <td>5.653675</td>
      <td>5.842247</td>
      <td>6.033506</td>
      <td>6.224445</td>
      <td>6.411483</td>
      <td>6.593974</td>
    </tr>
    <tr>
      <th>18</th>
      <td>7.456991</td>
      <td>7.299968</td>
      <td>7.113823</td>
      <td>6.908161</td>
      <td>6.689925</td>
      <td>6.470912</td>
      <td>6.264475</td>
      <td>6.166732</td>
      <td>6.108094</td>
      <td>6.254601</td>
      <td>...</td>
      <td>4.956514</td>
      <td>5.002743</td>
      <td>5.083952</td>
      <td>5.208605</td>
      <td>5.375140</td>
      <td>5.537127</td>
      <td>5.694327</td>
      <td>5.842809</td>
      <td>5.981164</td>
      <td>6.103932</td>
    </tr>
    <tr>
      <th>19</th>
      <td>6.842899</td>
      <td>6.703936</td>
      <td>6.547900</td>
      <td>6.382626</td>
      <td>6.212350</td>
      <td>6.051760</td>
      <td>5.910220</td>
      <td>5.793772</td>
      <td>5.722824</td>
      <td>5.770515</td>
      <td>...</td>
      <td>5.305710</td>
      <td>5.342902</td>
      <td>5.380088</td>
      <td>5.419069</td>
      <td>5.461800</td>
      <td>5.535933</td>
      <td>5.603478</td>
      <td>5.663849</td>
      <td>5.715477</td>
      <td>5.761320</td>
    </tr>
  </tbody>
</table>
<p>20 rows × 312 columns</p>
</div>




```python
fig, ax = plt.subplots()

# Make data.
X = freq2

#Y = np.linspace(0.7, 2, 9)
Y=np.arange(312)

X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
Z = plot22.T

# Plot the surface.
surf2 = ax.pcolormesh(Y, X, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel("times pwelch segments are averaged")
ax.set_ylabel("frequency")
#ax.set_zlabel("magnitude power")
plt.title("Spectrogram leftCheek")



# Add a color bar which maps values to colors.
fig.colorbar(surf2, shrink=0.5, aspect=5)
fig.set_size_inches(10, 10)


plt.show()

```

    C:\Users\maroa\anaconda3\envs\ml\lib\site-packages\ipykernel_launcher.py:15: MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
      from ipykernel import kernelapp as app
    


    
![png](output_4_1.png)
    



```python
plot3=pd.read_csv("Magnitude_avgrightCheek (8).csv", sep=";")
plot3.shape
plot31=plot3.iloc[:,1:313]
freq3=plot3.iloc[:,0]
plot31
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>magnitude2</th>
      <th>magnitude3</th>
      <th>magnitude4</th>
      <th>magnitude5</th>
      <th>magnitude6</th>
      <th>magnitude7</th>
      <th>magnitude8</th>
      <th>magnitude9</th>
      <th>magnitude10</th>
      <th>magnitude11</th>
      <th>...</th>
      <th>magnitude304</th>
      <th>magnitude305</th>
      <th>magnitude306</th>
      <th>magnitude307</th>
      <th>magnitude308</th>
      <th>magnitude309</th>
      <th>magnitude310</th>
      <th>magnitude311</th>
      <th>magnitude312</th>
      <th>magnitude313</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14.823950</td>
      <td>14.392173</td>
      <td>13.990439</td>
      <td>13.637152</td>
      <td>13.278962</td>
      <td>12.951694</td>
      <td>12.693126</td>
      <td>12.532382</td>
      <td>12.623238</td>
      <td>12.712913</td>
      <td>...</td>
      <td>21.789318</td>
      <td>21.850140</td>
      <td>21.879682</td>
      <td>22.028155</td>
      <td>21.958438</td>
      <td>21.898073</td>
      <td>21.771006</td>
      <td>21.570093</td>
      <td>21.341464</td>
      <td>21.057619</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.145943</td>
      <td>9.667320</td>
      <td>9.226372</td>
      <td>8.825587</td>
      <td>8.498967</td>
      <td>8.149539</td>
      <td>7.876050</td>
      <td>7.646316</td>
      <td>7.811693</td>
      <td>8.164484</td>
      <td>...</td>
      <td>14.668068</td>
      <td>14.628702</td>
      <td>14.787099</td>
      <td>14.727838</td>
      <td>14.924253</td>
      <td>15.041844</td>
      <td>15.133781</td>
      <td>15.210166</td>
      <td>15.241541</td>
      <td>15.298219</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15.236806</td>
      <td>14.974938</td>
      <td>14.682890</td>
      <td>14.366773</td>
      <td>14.044937</td>
      <td>13.765007</td>
      <td>13.446108</td>
      <td>13.227065</td>
      <td>13.245985</td>
      <td>13.272755</td>
      <td>...</td>
      <td>19.201678</td>
      <td>19.778685</td>
      <td>20.174629</td>
      <td>20.834489</td>
      <td>21.454367</td>
      <td>22.093319</td>
      <td>22.768165</td>
      <td>23.437315</td>
      <td>24.125720</td>
      <td>24.752824</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22.446884</td>
      <td>22.407153</td>
      <td>22.297877</td>
      <td>22.142243</td>
      <td>21.934477</td>
      <td>21.720600</td>
      <td>21.527116</td>
      <td>21.219340</td>
      <td>21.159881</td>
      <td>21.224001</td>
      <td>...</td>
      <td>8.495877</td>
      <td>8.913986</td>
      <td>9.455062</td>
      <td>10.147773</td>
      <td>10.852887</td>
      <td>11.790613</td>
      <td>12.748690</td>
      <td>13.772215</td>
      <td>14.798541</td>
      <td>15.880157</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.341362</td>
      <td>24.197333</td>
      <td>24.030305</td>
      <td>23.832301</td>
      <td>23.669458</td>
      <td>23.461483</td>
      <td>23.335972</td>
      <td>23.166656</td>
      <td>23.191899</td>
      <td>23.259047</td>
      <td>...</td>
      <td>12.157928</td>
      <td>12.564826</td>
      <td>13.225144</td>
      <td>13.691927</td>
      <td>14.423788</td>
      <td>15.024188</td>
      <td>15.658317</td>
      <td>16.259595</td>
      <td>16.870463</td>
      <td>17.418013</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.133595</td>
      <td>24.922040</td>
      <td>24.677799</td>
      <td>24.425405</td>
      <td>24.178840</td>
      <td>23.946774</td>
      <td>23.740545</td>
      <td>23.619373</td>
      <td>23.603404</td>
      <td>23.962081</td>
      <td>...</td>
      <td>12.537075</td>
      <td>12.751321</td>
      <td>13.017629</td>
      <td>13.288515</td>
      <td>13.516531</td>
      <td>13.725647</td>
      <td>13.866871</td>
      <td>13.941044</td>
      <td>13.907744</td>
      <td>13.794047</td>
    </tr>
    <tr>
      <th>6</th>
      <td>25.408094</td>
      <td>25.462417</td>
      <td>25.477493</td>
      <td>25.484759</td>
      <td>25.445333</td>
      <td>25.461318</td>
      <td>25.442359</td>
      <td>25.446338</td>
      <td>25.631715</td>
      <td>25.904113</td>
      <td>...</td>
      <td>10.150184</td>
      <td>10.327437</td>
      <td>10.492121</td>
      <td>10.694612</td>
      <td>10.912607</td>
      <td>11.142962</td>
      <td>11.367595</td>
      <td>11.596024</td>
      <td>11.833362</td>
      <td>12.078717</td>
    </tr>
    <tr>
      <th>7</th>
      <td>22.648086</td>
      <td>22.821937</td>
      <td>22.922177</td>
      <td>22.950996</td>
      <td>22.910681</td>
      <td>22.858899</td>
      <td>22.753914</td>
      <td>22.684582</td>
      <td>22.678587</td>
      <td>22.922417</td>
      <td>...</td>
      <td>11.152672</td>
      <td>11.119941</td>
      <td>11.185399</td>
      <td>11.230322</td>
      <td>11.376457</td>
      <td>11.523209</td>
      <td>11.697501</td>
      <td>11.896427</td>
      <td>12.097721</td>
      <td>12.314516</td>
    </tr>
    <tr>
      <th>8</th>
      <td>21.211000</td>
      <td>21.605389</td>
      <td>21.881721</td>
      <td>22.056283</td>
      <td>22.179265</td>
      <td>22.208887</td>
      <td>22.243501</td>
      <td>22.221744</td>
      <td>22.237281</td>
      <td>22.211585</td>
      <td>...</td>
      <td>9.509580</td>
      <td>9.391280</td>
      <td>9.266263</td>
      <td>9.215733</td>
      <td>9.108379</td>
      <td>9.080779</td>
      <td>9.053239</td>
      <td>9.034722</td>
      <td>9.045555</td>
      <td>9.063507</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.186279</td>
      <td>19.277381</td>
      <td>19.301064</td>
      <td>19.259773</td>
      <td>19.142096</td>
      <td>19.030093</td>
      <td>18.893139</td>
      <td>18.850401</td>
      <td>18.764744</td>
      <td>19.135590</td>
      <td>...</td>
      <td>9.165013</td>
      <td>9.071501</td>
      <td>8.888095</td>
      <td>8.667680</td>
      <td>8.493496</td>
      <td>8.217766</td>
      <td>7.928819</td>
      <td>7.634281</td>
      <td>7.326365</td>
      <td>7.054223</td>
    </tr>
    <tr>
      <th>10</th>
      <td>16.480299</td>
      <td>16.273050</td>
      <td>16.043845</td>
      <td>15.803365</td>
      <td>15.585560</td>
      <td>15.373278</td>
      <td>15.152239</td>
      <td>15.050121</td>
      <td>15.016179</td>
      <td>15.063532</td>
      <td>...</td>
      <td>9.413730</td>
      <td>9.285724</td>
      <td>9.094712</td>
      <td>8.898163</td>
      <td>8.743466</td>
      <td>8.538589</td>
      <td>8.319601</td>
      <td>8.102170</td>
      <td>7.883820</td>
      <td>7.655277</td>
    </tr>
    <tr>
      <th>11</th>
      <td>14.457102</td>
      <td>14.166891</td>
      <td>13.883231</td>
      <td>13.622891</td>
      <td>13.406260</td>
      <td>13.184419</td>
      <td>13.011100</td>
      <td>12.903177</td>
      <td>12.834436</td>
      <td>12.913226</td>
      <td>...</td>
      <td>6.307038</td>
      <td>6.240630</td>
      <td>6.187995</td>
      <td>6.135793</td>
      <td>6.087401</td>
      <td>6.059970</td>
      <td>6.042300</td>
      <td>6.030429</td>
      <td>6.027523</td>
      <td>6.045491</td>
    </tr>
    <tr>
      <th>12</th>
      <td>11.056685</td>
      <td>10.880449</td>
      <td>10.709010</td>
      <td>10.546935</td>
      <td>10.377489</td>
      <td>10.228378</td>
      <td>10.131047</td>
      <td>10.076128</td>
      <td>10.014213</td>
      <td>10.202908</td>
      <td>...</td>
      <td>6.741228</td>
      <td>6.785923</td>
      <td>6.833634</td>
      <td>6.921355</td>
      <td>7.020479</td>
      <td>7.088950</td>
      <td>7.138067</td>
      <td>7.170385</td>
      <td>7.180280</td>
      <td>7.154415</td>
    </tr>
    <tr>
      <th>13</th>
      <td>8.851141</td>
      <td>8.831193</td>
      <td>8.797858</td>
      <td>8.755730</td>
      <td>8.689210</td>
      <td>8.652279</td>
      <td>8.642226</td>
      <td>8.642719</td>
      <td>8.666990</td>
      <td>8.781101</td>
      <td>...</td>
      <td>5.123415</td>
      <td>5.316705</td>
      <td>5.454112</td>
      <td>5.562101</td>
      <td>5.720052</td>
      <td>5.882031</td>
      <td>6.028291</td>
      <td>6.151223</td>
      <td>6.254506</td>
      <td>6.349843</td>
    </tr>
    <tr>
      <th>14</th>
      <td>7.268345</td>
      <td>7.251881</td>
      <td>7.212866</td>
      <td>7.162885</td>
      <td>7.116259</td>
      <td>7.080842</td>
      <td>7.040274</td>
      <td>7.075009</td>
      <td>7.091409</td>
      <td>7.167250</td>
      <td>...</td>
      <td>2.985583</td>
      <td>3.109668</td>
      <td>3.312370</td>
      <td>3.550121</td>
      <td>3.731246</td>
      <td>3.959804</td>
      <td>4.194270</td>
      <td>4.432982</td>
      <td>4.669147</td>
      <td>4.885631</td>
    </tr>
    <tr>
      <th>15</th>
      <td>6.504845</td>
      <td>6.498456</td>
      <td>6.473571</td>
      <td>6.435154</td>
      <td>6.400948</td>
      <td>6.345241</td>
      <td>6.284675</td>
      <td>6.311600</td>
      <td>6.349278</td>
      <td>6.537907</td>
      <td>...</td>
      <td>4.586837</td>
      <td>4.792301</td>
      <td>5.050277</td>
      <td>5.385700</td>
      <td>5.786143</td>
      <td>6.106560</td>
      <td>6.415257</td>
      <td>6.706373</td>
      <td>6.976376</td>
      <td>7.229126</td>
    </tr>
    <tr>
      <th>16</th>
      <td>6.490016</td>
      <td>6.515479</td>
      <td>6.507104</td>
      <td>6.474517</td>
      <td>6.404415</td>
      <td>6.336192</td>
      <td>6.282662</td>
      <td>6.251171</td>
      <td>6.283364</td>
      <td>6.469351</td>
      <td>...</td>
      <td>2.855786</td>
      <td>3.018950</td>
      <td>3.176656</td>
      <td>3.339850</td>
      <td>3.539075</td>
      <td>3.827920</td>
      <td>4.121745</td>
      <td>4.416380</td>
      <td>4.705202</td>
      <td>4.978035</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7.062388</td>
      <td>6.994011</td>
      <td>6.906216</td>
      <td>6.805327</td>
      <td>6.721637</td>
      <td>6.634763</td>
      <td>6.550065</td>
      <td>6.489497</td>
      <td>6.442366</td>
      <td>6.496994</td>
      <td>...</td>
      <td>5.640479</td>
      <td>5.851298</td>
      <td>6.081511</td>
      <td>6.318125</td>
      <td>6.549896</td>
      <td>6.759505</td>
      <td>6.966731</td>
      <td>7.166709</td>
      <td>7.354431</td>
      <td>7.530278</td>
    </tr>
    <tr>
      <th>18</th>
      <td>6.779054</td>
      <td>6.723312</td>
      <td>6.653888</td>
      <td>6.576597</td>
      <td>6.486060</td>
      <td>6.398737</td>
      <td>6.322424</td>
      <td>6.320063</td>
      <td>6.320788</td>
      <td>6.421042</td>
      <td>...</td>
      <td>5.625649</td>
      <td>5.646633</td>
      <td>5.704197</td>
      <td>5.804208</td>
      <td>5.946990</td>
      <td>6.082938</td>
      <td>6.212332</td>
      <td>6.334392</td>
      <td>6.445820</td>
      <td>6.540922</td>
    </tr>
    <tr>
      <th>19</th>
      <td>6.911902</td>
      <td>6.869958</td>
      <td>6.824953</td>
      <td>6.781264</td>
      <td>6.724638</td>
      <td>6.680615</td>
      <td>6.652702</td>
      <td>6.682449</td>
      <td>6.751004</td>
      <td>6.923796</td>
      <td>...</td>
      <td>5.634312</td>
      <td>5.639803</td>
      <td>5.645323</td>
      <td>5.649394</td>
      <td>5.654645</td>
      <td>5.695960</td>
      <td>5.729725</td>
      <td>5.754781</td>
      <td>5.770368</td>
      <td>5.779993</td>
    </tr>
  </tbody>
</table>
<p>20 rows × 312 columns</p>
</div>




```python
fig, ax = plt.subplots()

# Make data.
X = freq
#Y = np.linspace(0.7, 2, 9)
Y=np.arange(312)


X, Y = np.meshgrid(X, Y)
Z = plot31.T

# Plot the surface.
surf3 = ax.pcolormesh(Y, X, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


ax.set_xlabel("times pwelch segments are averaged")
ax.set_ylabel("frequency")
plt.title("Spectrogram rightCheek")



# Add a color bar which maps values to colors.
fig.colorbar(surf3, shrink=0.5, aspect=5)
fig.set_size_inches(10, 10)


plt.show()

```

    C:\Users\maroa\anaconda3\envs\ml\lib\site-packages\ipykernel_launcher.py:14: MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
      
    


    
![png](output_6_1.png)
    



```python
allmag=pd.read_csv("Magnitude_forehead (7).csv", sep=";")
allmag.shape
```




    (257, 344)




```python
fig, ax = plt.subplots()

# Make data.
X = np.arange(344)
Y = np.arange(77)
X, Y = np.meshgrid(X, Y)

allmag=np.array(allmag)
#Z = allmag[:,100:].T
Z=allmag[:-180]
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

    C:\Users\maroa\anaconda3\envs\ml\lib\site-packages\ipykernel_launcher.py:15: MatplotlibDeprecationWarning: shading='flat' when X and Y have the same dimensions as C is deprecated since 3.3.  Either specify the corners of the quadrilaterals with X and Y, or pass shading='auto', 'nearest' or 'gouraud', or set rcParams['pcolor.shading'].  This will become an error two minor releases later.
      from ipykernel import kernelapp as app
    


    
![png](output_8_1.png)
    



```python

```


```python

```
