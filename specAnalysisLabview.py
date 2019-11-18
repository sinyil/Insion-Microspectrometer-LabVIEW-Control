# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pandas as pd
import matplotlib.pyplot as plt

# to clean the .txt file by getting rid of experiment information.
filename = 'log_OD.txt'

# Unnecessary since our log_OD is already cleaned up by LabVIEW.
#txtRead = open(filename)
#cont = txtRead.read()
#txtRead.close()
#b = cont.split('\n',1)[1]
#print(b,  file=open('dummy.txt', 'w'))

# to get the raw data from cleaned .txt file
data = pd.read_csv(filename, sep='\t')
print(data)

# Unnecessary since the data already has wavelength on its x-axis.
#for k in range(0,len(data.columns),2):
#    data.iloc[:,k] = -0.000014*data.iloc[:,k]**2 + 2.0117*data.iloc[:,k] - 1248.8670

# to plot the data recevied between two wavelengths
fig, ax = plt.subplots(1,1, figsize=(17,10))

for i in range(4,len(data.columns),2):
    ax.plot(data.iloc[:,i], data.iloc[:,i+1], label=data.columns[i+1])
ax.legend(loc='best', frameon=True); plt.xlabel('Wavelength (nm)'); plt.ylabel('Absorbance [AU]')
plt.savefig(filename[:-4] + '.png', format='png')
plt.show()